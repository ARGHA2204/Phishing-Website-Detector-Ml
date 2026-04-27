# Phishing Website Detector (Machine Learning)

## Overview
This project is a full-stack web application that detects phishing websites using machine learning. The system analyzes URL-based features and predicts whether a website is legitimate or malicious.

---

## Features
- Input any website URL
- Extracts important URL features
- Uses a trained ML model for prediction
- Classifies website as phishing or legitimate
- Simple web interface for interaction

---

## Tech Stack
- Backend: Python, Flask
- Machine Learning: Scikit-learn (Random Forest)
- Frontend: HTML, CSS, JavaScript

---

## Project Structure
Phishing-Website-Detector-Ml/
│
├── backend/
│ ├── app.py
│ ├── model.py
│ ├── features.py
│ ├── train_model.py
│ ├── model.pkl
│ ├── requirements.txt
│
├── frontend/
│ ├── index.html
│ ├── style.css
│ ├── script.js
│
├── dataset/
│ ├── phishing.csv
│
├── README.md
├── LICENSE
└── .gitignore



---

## How to Run

### 1. Clone the repository


git clone https://github.com/ARGHA2204/Phishing-Website-Detector-Ml.git

cd phishing-website-detector-ml


---

### 2. Setup backend

cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python train_model.py
python app.py


---

### 3. Run frontend
Open a new terminal:

cd frontend
python -m http.server 5500


Then open:

http://localhost:5500


---

## Sample Inputs

Phishing examples:
- http://secure-login-bank.com
- http://verify-paypal-account.com

Legitimate examples:
- https://google.com
- https://github.com

---

## Sample Output


Input: http://secure-login-bank.com

Result: Phishing Website

Input: https://google.com

Result: Legitimate Website
















