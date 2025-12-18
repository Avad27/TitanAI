import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import joblib

print("Loading TitanAI dataset...")
data = pd.read_csv("titanai_large_transactions.csv")

# Separate features and label
X = data.drop(["transaction_id", "is_fraud"], axis=1)
y = data["is_fraud"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# ML Pipeline (scaling + model)
model = Pipeline([
    ("scaler", StandardScaler()),
    ("rf", RandomForestClassifier(
        n_estimators=60,
        max_depth=10,
        random_state=42
    ))
])

print("Training fraud detection model...")
model.fit(X_train, y_train)

joblib.dump(model, "fraud_model.pkl")

print("Model training completed successfully.")
print("Model saved as fraud_model.pkl")