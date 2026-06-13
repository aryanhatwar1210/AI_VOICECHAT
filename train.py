import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

data = pd.read_csv("command.csv")

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data["text"])

model = LogisticRegression()
model.fit(X, data["intent"])

joblib.dump(model, "intent_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model Trained Successfully")