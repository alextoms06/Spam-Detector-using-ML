# retrain_export_model.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import json

# -------------------------------
# Step 1: Load your dataset
# -------------------------------
# Make sure your CSV has columns: 'label' and 'text'
# 'label' values: 'spam' or 'ham'
df = pd.read_csv('spam.csv')

# Convert labels to numeric
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# -------------------------------
# Step 2: Split into train/test
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    df['text'], df['label'], test_size=0.2, random_state=42
)

# -------------------------------
# Step 3: Binary TF-IDF Vectorizer
# -------------------------------
vectorizer = TfidfVectorizer(binary=True)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# -------------------------------
# Step 4: Train Logistic Regression
# -------------------------------
model = LogisticRegression()
model.fit(X_train_vec, y_train)

# Evaluate accuracy
y_pred = model.predict(X_test_vec)
print("✅ Accuracy on test set:", accuracy_score(y_test, y_pred))

# -------------------------------
# Step 5: Export for Chrome Extension
# -------------------------------
# Export vocabulary
vocab = vectorizer.get_feature_names_out().tolist()
with open('vocab.json', 'w') as f:
    json.dump(vocab, f)

# Export model coefficients and intercept
model_data = {
    'coef': model.coef_[0].tolist(),
    'intercept': model.intercept_[0].tolist()
}
with open('model.json', 'w') as f:
    json.dump(model_data, f)

print("✅ Exported vocab.json and model.json successfully!")
