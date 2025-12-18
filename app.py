from flask import Flask, request, jsonify
import pandas as pd
import joblib
from utils.decision_engine import make_decision

app = Flask(__name__)

# Load trained model
model = joblib.load("fraud_model.pkl")

@app.route("/")
def home():
    return {
        "message": "TitanAI Fraud Detection Engine is running successfully"
    }

@app.route("/analyze", methods=["POST"])
def analyze_transaction():
    """
    Expects JSON with:
    amount, transaction_hour, kyc_level,
    device_change, location_change, past_fraud_count
    """

    data = request.json

    df = pd.DataFrame([data])

    fraud_probability = model.predict_proba(df)[0][1]

    decision_data = make_decision(fraud_probability)

    return jsonify({
        "fraud_probability": round(fraud_probability, 3),
        **decision_data
    })

if __name__ == "__main__":
    app.run(debug=True)