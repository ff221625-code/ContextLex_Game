from flask import Flask, render_template, jsonify, request
from pathlib import Path
from collections import defaultdict
import csv, random, re, socket, os

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent
DATASET_PATH = BASE_DIR / "wsd_dataset.csv"
STOP_WORDS = {"the", "a", "an", "is", "are", "was", "were", "and", "or", "to", "of", "in", "on", "at", "for", "with", "by", "from", "it", "this", "that", "he", "she", "they", "we", "i", "you", "his", "her", "their", "my", "our", "as", "be", "been", "being", "its"}


def load_dataset():
    rows = []
    with DATASET_PATH.open(encoding="utf-8-sig", newline="") as file:
        for row in csv.DictReader(file):
            sentence = (row.get("sentence") or "").strip()
            word = (row.get("target_word") or "").strip().lower()
            sense = (row.get("sense") or "").strip()
            meaning = (row.get("meaning") or "").strip()
            if sentence and word and sense and meaning:
                rows.append({"sentence": sentence, "word": word, "sense": sense, "meaning": meaning})
    return rows

DATASET = load_dataset()
BY_WORD = defaultdict(list)
for item in DATASET:
    BY_WORD[item["word"]].append(item)


def tokens(text):
    return {w for w in re.findall(r"[a-z]+", text.lower()) if len(w) > 2 and w not in STOP_WORDS}


def make_question(row):
    meanings = list(dict.fromkeys(x["meaning"] for x in BY_WORD[row["word"]]))
    correct = row["meaning"]
    distractors = [m for m in meanings if m != correct]
    if len(distractors) < 2:
        distractors += [x["meaning"] for x in DATASET if x["meaning"] != correct and x["meaning"] not in distractors]
    options = [correct] + random.sample(distractors, 2)
    random.shuffle(options)
    return {"word": row["word"], "sentence": row["sentence"], "options": options,
            "answer": options.index(correct), "explanation": f'In this sentence, "{row["word"]}" means {correct}.'}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/questions")
def questions():
    if len(DATASET) < 10:
        return jsonify({"error": "Not enough word challenges are available yet."}), 500
    available_words = list(BY_WORD.keys())
    selected_words = random.sample(available_words, min(10, len(available_words)))
    chosen = [random.choice(BY_WORD[word]) for word in selected_words]
    return jsonify({"questions": [make_question(row) for row in chosen]})


@app.route("/api/free-play", methods=["POST"])
def free_play():
    data = request.get_json(silent=True) or {}
    sentence = str(data.get("sentence", "")).strip()
    target = str(data.get("target", "")).strip().lower()
    if not sentence:
        return jsonify({"error": "Please enter a sentence."}), 400
    if target and not re.search(r"\b" + re.escape(target) + r"\b", sentence, re.I):
        return jsonify({"error": f'The target word "{target}" is not in your sentence.'}), 400
    if not target:
        found = [w for w in BY_WORD if re.search(r"\b" + re.escape(w) + r"\b", sentence, re.I)]
        if len(found) == 1:
            target = found[0]
        elif len(found) > 1:
            return jsonify({"error": "More than one dataset word was found. Please enter the target word you want to analyze."}), 400
        else:
            return jsonify({"error": "Please enter a target word that exists in the dataset, such as bat, bank, crane, mouse, or wave."}), 400
    candidates = BY_WORD.get(target, [])
    if not candidates:
        return jsonify({"error": f'"{target}" is not currently included in the dataset. Try another target word.'}), 400

    input_words = tokens(sentence)
    sense_scores = defaultdict(float)
    sense_examples = defaultdict(list)
    for row in candidates:
        example_words = tokens(row["sentence"])
        overlap = input_words & (example_words - {target})
        # Weighted overlap: rare, informative shared words matter more than sentence length.
        score = len(overlap) / max(1, len(input_words | (example_words - {target})))
        if overlap:
            sense_scores[row["sense"]] = max(sense_scores[row["sense"]], score)
            sense_examples[row["sense"]].append((score, row, sorted(overlap)))
    if not sense_scores or max(sense_scores.values()) < 0.08:
        return jsonify({"target": target, "meaning": "Not confident enough to decide", "explanation": "I found the target word, but the sentence does not contain enough clues that match the dataset. Try adding more context."})
    ranked = sorted(sense_scores.items(), key=lambda x: x[1], reverse=True)
    best_sense, best_score = ranked[0]
    if len(ranked) > 1 and abs(best_score - ranked[1][1]) < 0.025:
        return jsonify({"target": target, "meaning": "Ambiguous context", "explanation": "The clues could fit more than one meaning. Add a few more details to your sentence."})
    best_row = max(sense_examples[best_sense], key=lambda x: x[0])[1]
    clues = max(sense_examples[best_sense], key=lambda x: x[0])[2]
    return jsonify({"target": target, "meaning": best_row["meaning"],
                    "explanation": "Context clues found: " + ", ".join(clues[:6]) + ". These clues support this meaning.",
                    "sense": best_sense})


if __name__ == "__main__":
    # Local development uses port 5001; hosting platforms provide PORT.
    port = int(os.environ.get("PORT", "5001"))
    app.run(host="0.0.0.0", port=port, debug=False)
