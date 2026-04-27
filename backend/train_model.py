import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
from features import extract_features

df = pd.read_csv("../dataset/phishing.csv")

X = df['url'].apply(extract_features).tolist()
y = df['label']

model = RandomForestClassifier()
model.fit(X, y)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved!")