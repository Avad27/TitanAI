def make_decision(fraud_probability):
    risk_score = int(fraud_probability * 100)
    explanation = []

    if risk_score >= 80:
        decision = "BLOCK"
        explanation.append("High-risk transaction pattern detected")
    elif risk_score >= 50:
        decision = "OTP_REQUIRED"
        explanation.append("Suspicious transaction, additional verification required")
    else:
        decision = "APPROVE"
        explanation.append("Transaction behavior within normal limits")

    return {
        "risk_score": risk_score,
        "decision": decision,
        "explanation": explanation
    }