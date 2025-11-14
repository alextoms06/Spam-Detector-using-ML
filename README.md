# Spam-Detector-using-ML
CHROME EXTENSION BRNACH- YOU'LL NEED ALL OF THIS
How I Built This Project (Step by Step)

Trained Model in Colab

Loaded the spam dataset (spam.csv).

Preprocessed text and labels.

Used TfidfVectorizer and LogisticRegression.

Trained the model, tested accuracy.

Saved & Exported Model

Saved model as spam_model.pkl.

Saved vectorizer as vectorizer.pkl.

Exported model.json and vocab.json for use in the extension.

Created Chrome Extension Files

manifest.json → metadata for Chrome (permissions, popup file).

popup.html → user interface (text input and result).

popup.js → loads exported model & vocabulary, handles input, shows prediction.

icon.png → extension toolbar icon.

Tested Extension Locally

Opened chrome://extensions/ in Chrome.

Enabled Developer mode.

Clicked Load unpacked and selected the AI_extension folder.

Typed test messages in the popup and checked predictions.

Optional: Retraining

Used retrain.py in Python to update spam_model.pkl and vectorizer.pkl.

Exported again to model.json and vocab.json for the extension.




How it Works

Text entered in the popup is vectorized using vocab.json.

The exported model (model.json) predicts spam probability.

Result is displayed immediately in the popup.

Notes

Make sure the model and vocab files match the version of the extension.

The extension runs locally in Chrome; it does not require a server.





*Files in the Chrome Extension + ML project*

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
