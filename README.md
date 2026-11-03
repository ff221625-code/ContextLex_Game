# 🎮🎯ContextLex – The Word Meaning Challenge Game 

## Explore Words. Discover Meanings. Understand Context.

ContextLex is an interactive, context-aware Natural Language Processing (NLP) web application designed to make language learning engaging. It helps users understand how the meaning of a word changes depending on the context in which it is used.

The application combines interactive word challenges with NLP techniques such as Word Sense Disambiguation, Semantic Role Analysis, and N-gram-based Next Word Prediction.

---

## ✨Features

1. Word Meaning Quiz

- Interactive multiple-choice questions.
- Identify the correct meaning of words based on sentence context.
- Instant feedback for answers.
- Score tracking and quiz restart option.

2. Free Play – Context Analysis

- Enter your own sentences.
- Explore the meaning of words in different contexts.
- Understand how context influences word meaning.

3. Word Sense Disambiguation (WSD)

- Identifies the intended meaning of ambiguous words.
- Uses surrounding words and sentence context.
- Uses a curated dataset for word meaning analysis.

4. Semantic Role Analysis

- Analyses the roles played by words and phrases in a sentence.
- Helps understand sentence structure and relationships.

5. Next Word Prediction

- Predicts possible next words based on the given text.
- Uses an N-gram language model.
- Demonstrates basic language prediction concepts.

---

## 🛠️Technologies Used

Technology| Purpose
Python| Backend programming
Flask| Web application framework
HTML| Web page structure
CSS| Styling and responsive design
JavaScript| Interactive functionality
NLP| Language analysis
N-gram| Next-word prediction
Git & GitHub| Version control
Render| Web application deployment

---

## 💾Project Structure

```
ContextLex_Game/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── wsd_dataset.csv
```

Note: "wsd_dataset.csv" is a private dataset. It is excluded from the public GitHub repository and configured separately on Render using Secret Files.

---

## ⚙️Installation and Setup

Follow these steps to run ContextLex on your computer.

Step 1: Clone the Repository

`git clone https://github.com/ff221625-code/ContextLex_Game.git`

Step 2: Open the Project Folder

`cd ContextLex_Game`

Step 3: Create a Virtual Environment

`python -m venv venv`

Step 4: Activate the Virtual Environment

For Windows PowerShell:

`venv\Scripts\activate`

Step 5: Install Required Packages

`pip install -r requirements.txt`

Step 6: Add the Private Dataset

Place your private `"wsd_dataset.csv"` file in the main project folder, alongside `"app.py"`, before running the application locally.

The dataset is not included in the public GitHub repository.

Step 7: Run the Application

`python app.py`

Open the local URL displayed in your terminal to access ContextLex.

---

## 🔗Deployment

ContextLex is deployed using Render.

Live Website:

`https://contextlex-game.onrender.com`

GitHub Repository:

`https://github.com/ff221625-code/ContextLex_Game`

Render Configuration
`
Configuration| Value
Runtime| Python 3
Build Command| "pip install -r requirements.txt"
Start Command| "gunicorn app:app"
Branch| "main"
` 

Private Dataset Configuration

The WSD dataset is configured through Render's Environment → Secret Files section.

Filename:

`"wsd_dataset.csv"`

This keeps the dataset separate from the public GitHub repository.

---

## 📑Applications

- Understanding ambiguous words in natural language.
- Learning context-based word meanings.
- Exploring basic Natural Language Processing concepts.
- Understanding semantic roles in sentences.
- Demonstrating simple language prediction techniques.

---

## 🚀Future Enhancements

- Expand the word meaning database.
- Improve contextual word analysis.
- Support more languages.
- Enhance prediction accuracy.
- Introduce additional NLP-based learning activities.
- Improve the user experience with more interactive features.

---

## 👩🏻‍💻Author Firdous Fathima 

ContextLex – The Word Meaning Challenge

An interactive Context-Aware NLP Learning Platform.

Where Words Meet Context and Meaning.
