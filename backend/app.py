from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
from features import extract_features

app = Flask(__name__)
CORS(app)

model = pickle.load(open("model.pkl", "rb"))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    url = data['url']

    features = extract_features(url)
    prediction = model.predict([features])[0]

    result = "Phishing Website" if prediction == 1 else "Legitimate Website"

    return jsonify({
        "result": result
    })

if __name__ == "__main__":
    app.run(debug=True)