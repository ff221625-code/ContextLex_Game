# ContextLex — Context-Aware Word Meaning Challenge

ContextLex is a Flask-based educational NLP application featuring:
- A multiple-choice word-meaning quiz.
- A free-play contextual word meaning analyzer.
- A curated word-sense example collection covering 32 words, with at least three distinct senses per word and four example sentences per sense.

## Run locally
1. Install Python 3.10 or newer.
2. Open this folder in VS Code.
3. Create/activate a virtual environment (optional but recommended).
4. Install dependencies: `pip install -r requirements.txt`
5. Start the app: `python app.py`
6. Open the local URL printed in the terminal.

## Deployment
Use a Python-capable host for the Flask application. GitHub stores the source code; GitHub Pages alone cannot run this Flask backend.

## Project data
The word-sense examples are stored in `wsd_dataset.csv` and used by the backend for contextual matching. Do not describe the application as using no dataset. Check the source/licence of any third-party data before publishing; this CSV is a curated project dataset.
