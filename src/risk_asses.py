import numpy as np
import joblib
import os
import pandas as pd

class RiskAssessmentEngine:
    """
    RiskAssessmentEngine calculates risk scores for drivers
    using a trained ML model (GLM) or a fallback heuristic.
    """

    def __init__(self):
        # Define paths
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        MODEL_DIR = os.path.join(BASE_DIR, "model and data")
        self.model_path = os.path.join(MODEL_DIR, "glm_risk_model.pkl")
        self.scaler_path = os.path.join(MODEL_DIR, "risk_scaler.pkl")

        # Load model and scaler
        try:
            print("Loading Trained GLM Risk Model...")
            self.model = joblib.load(self.model_path)
            self.scaler = joblib.load(self.scaler_path)
            self.ml_available = True
        except Exception as e:
            print("❌ ERROR: ML model files not found. Using dummy risk estimation.")
            print(f"Reason: {e}")
            self.ml_available = False

    def calculate_risk(self, data):
        """
        Calculate risk score for a single driver.
        data: dict with keys ["Driver Age", "Previous Accidents", "Annual Mileage (x1000 km)"]
        Returns a float risk score rounded to 2 decimals.
        """
        age = data.get("Driver Age", 30)
        accidents = data.get("Previous Accidents", 0)
        mileage = data.get("Annual Mileage (x1000 km)", 10)

        X = np.array([[age, accidents, mileage]])

        if self.ml_available:
            # Ensure feature order matches training
            X_scaled = self.scaler.transform(X)
            risk_score = self.model.predict(X_scaled)[0]
        else:
            # Fallback heuristic
            risk_score = (accidents * 1.8) + (mileage * 0.05) + (age * 0.02)

        return round(float(risk_score), 2)

    def calculate_risk_batch(self, df):
        """
        Optional: calculate risk scores for a DataFrame.
        df: pandas DataFrame with columns ["Driver Age", "Previous Accidents", "Annual Mileage (x1000 km)"]
        Returns a pandas Series of risk scores.
        """
        risk_scores = []
        for _, row in df.iterrows():
            data_dict = {
                "Driver Age": row.get("Driver Age", 30),
                "Previous Accidents": row.get("Previous Accidents", 0),
                "Annual Mileage (x1000 km)": row.get("Annual Mileage (x1000 km)", 10)
            }
            risk_scores.append(self.calculate_risk(data_dict))
        return pd.Series(risk_scores, index=df.index)
