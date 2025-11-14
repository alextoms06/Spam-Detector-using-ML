from flask import Flask, request, jsonify, render_template, render_template_string
from flask_cors import CORS
import pickle


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Load model + vectorizer
with open('spam_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

app = Flask(__name__)
CORS(app)

# Simple HTML form
HTML_PAGE = """
<!doctype html>
<html>
<head>
    <title>Spam Mail Detector</title>
    <style>
        body {font-family: Arial; background:#121212; color:white; text-align:center; margin-top:100px;}
        input, textarea {width:300px; padding:10px; margin:10px; border-radius:5px; border:none;}
        button {padding:10px 20px; background:#4CAF50; color:white; border:none; border-radius:5px;}
        button:hover {background:#45a049;}
        .box {background:#1e1e1e; display:inline-block; padding:30px; border-radius:15px;}
    </style>
</head>
<body>
    <div class="box">
        <h2>📧 Spam Mail Classifier</h2>
        <form method="POST">
            <textarea name="message" rows="5" placeholder="Paste email text here..."></textarea><br>
            <button type="submit">Check</button>
        </form>
        {% if prediction is not none %}
            <h3>Result: {{ prediction }}</h3>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None
    if request.method == 'POST':
        message = request.form['message']
        data = vectorizer.transform([message])
        result = model.predict(data)[0]
        prediction = "🚫 Spam" if result == 1 else "✅ Not Spam"
    return render_template_string(HTML_PAGE, prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
