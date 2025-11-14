# Spam-Detector-using-ML
The only files you'll need in WEBAPP are------ 
MAIL.py, spam_model.pkl, vectorizer.pkl



# Spam Detector Web App

A simple web application built with **Python and Flask** to classify text messages as **spam** or **not spam** using a trained machine learning model.

---
How I Built This Project

Started in Google Colab

Imported libraries: pandas, sklearn, pickle, etc.

Loaded the spam dataset (spam.csv) for training.

Preprocessed Data

Converted text labels (spam/ham) to numbers.

Split data into training and testing sets.

Trained the ML Model

Used TfidfVectorizer for text vectorization.

Trained LogisticRegression on the dataset.

Tested accuracy and saved results.

Saved the Model & Vectorizer

Saved trained model as spam_model.pkl.

Saved trained vectorizer as vectorizer.pkl.

Exported for Web App

Created main.py to load the model and vectorizer.

Built a Flask web app with a simple input form (index.html).

Tested Locally

Ran main.py in VS Code.

Checked predictions via browser at http://127.0.0.1:5000.

Optional: Retraining

Used retrain.py to retrain the model with new data when needed.

## **Features**

* Enter any text message and get instant **spam/not spam prediction**.
* Uses a **trained Logistic Regression model** with Tfidf vectorization.
* Easy to run locally and test.



2. Open your browser and go to:

```
http://127.0.0.1:5000
```

3. Enter text in the input box and click **Check** to see if it’s spam or not.

---

## **How it Works**

1. Text input is **converted to numerical features** using the Tfidf vectorizer (`vectorizer.pkl`).
2. The trained **Logistic Regression model (`spam_model.pkl`)** predicts whether the text is spam.
3. The result is displayed on the webpage instantly.

---

## **Retraining the Model**

* You can retrain the model using **`retrain.py`** with your own dataset of messages.
* Save the updated `spam_model.pkl` and `vectorizer.pkl` to use in the app.

---

## **Dependencies**

* Python 3.x
* Flask
* scikit-learn
* pandas
* numpy



