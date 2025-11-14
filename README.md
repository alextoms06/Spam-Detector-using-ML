# Spam-Detector-using-ML
CHROME EXTENSION BRNACH- YOU'LL NEED ALL OF THIS

Files in the Chrome Extension + ML project

icon.png

The small image that appears in the Chrome toolbar for the extension.

imports.py

Python helper file that loads the trained ML model and vectorizer for the web app or backend.

manifest.json

Metadata for your Chrome extension: name, version, permissions, scripts, and popup file.

model.json

Exported ML model in JSON format (used by JavaScript in the extension).

popup.html

The HTML page displayed when you click the extension icon; contains the input box and buttons.

popup.js

JavaScript code for the extension; sends text input, processes it with the model, and shows results.

retrain.py

Python script used to retrain the spam detection model with new data.

spam_model.pkl

Trained Logistic Regression model stored in Python pickle format (used for the web app).

vectorizer.pkl

Trained text vectorizer (TfidfVectorizer) stored in Python pickle format; converts text into numbers for ML.

vocab.json

Vocabulary of words used by the model (exported for JavaScript/extension).
