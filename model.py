import pickle
from utils import clean_text

# Load model
with open("phishing_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load vectorizer
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

def predict_email(email_text):
    vect_text = vectorizer.transform([clean_text(email_text)])
    prediction = model.predict(vect_text)[0]
    return prediction





