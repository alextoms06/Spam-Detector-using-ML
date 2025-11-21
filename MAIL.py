from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# ==========================
# Load Model + Vectorizer
# ==========================
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)


# ==========================
# Home Route
# ==========================
@app.route("/", methods=["GET"])
def home():
    return {"message": "Mail Classifier API is running!"}


# ==========================
# Prediction Route
# ==========================
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    if "text" not in data:
        return jsonify({"error": "Missing 'text' field"}), 400

    email_text = data["text"]
    vect = vectorizer.transform([email_text])
    pred = model.predict(vect)[0]

    return jsonify({"prediction": pred})


# ==========================
# Run app (for local testing)
# ==========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
