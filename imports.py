import pickle
import json

# Load your existing model and vectorizer
model = pickle.load(open('spam_model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# Export vocabulary
vocab = vectorizer.get_feature_names_out().tolist()
with open('vocab.json', 'w') as f:
    json.dump(vocab, f)

# Export coefficients and intercept
model_data = {
    'coef': model.coef_[0].tolist(),
    'intercept': model.intercept_[0].tolist()
}
with open('model.json', 'w') as f:
    json.dump(model_data, f)

print("✅ Exported vocab.json and model.json successfully!")
