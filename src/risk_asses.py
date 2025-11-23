import random
from typing import Dict, Any, Tuple
import joblib
import numpy as np
import warnings

# --- Risk Assessment Engine (OOP) ---
# Uses a trained Logistic Regression (GLM) model to generate risk score.

class RiskAssessmentEngine:
    """
    Calculates a personalized risk score based on applicant's static data
    using a trained Logistic Regression Model (GLM).
    """

    MODEL_FEATURES: list = ['Driver Age', 'Previous Accidents', 'Annual Mileage (x1000 km)']
    MAX_RISK_SCORE: float = 10.0

    def __init__(self):
        print("Loading Trained GLM Risk Model...")
        try:
            self.model = joblib.load('glm_risk_model.pkl')
            self.scaler = joblib.load('risk_scaler.pkl')
            self.risk_threshold = np.load('risk_threshold.npy').item()
            print("GLM Model, Scaler, and Threshold loaded successfully.")
        except FileNotFoundError:
            print("ERROR: ML model files not found. Using dummy risk estimation.")
            self.model = None
            self.scaler = None
            self.risk_threshold = 493.95

    def calculate_risk_score(self, applicant_data: Dict[str, Any]) -> Tuple[float, str]:

        input_data = np.array([[ 
            applicant_data.get('Driver Age', 30),
            applicant_data.get('Previous Accidents', 0),
            applicant_data.get('Annual Mileage (x1000 km)', 15)
        ]])

        if self.model is None:
            predicted_risk_prob = 0.5
        else:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                scaled_data = self.scaler.transform(input_data)
                predicted_risk_prob = self.model.predict_proba(scaled_data)[0][1]

        risk_score = predicted_risk_prob * self.MAX_RISK_SCORE

        age, claims, mileage = input_data[0]

        if claims > 2:
            main_driver = f"Very High Claims ({claims:.0f})"
        elif age < 25 or age > 60:
            main_driver = f"Age ({age:.0f}) outside optimal bracket"
        elif mileage > 25:
            main_driver = f"High Annual Mileage ({mileage:.0f}k km)"
        else:
            main_driver = "Favorable / Average Profile"

        explanation = f"""
Risk Assessment Summary (Logistic Regression Model):
- Prediction Method: GLM (Logistic Regression)
- Predicted High-Risk Probability: {predicted_risk_prob:.4f}
- Risk Threshold Reference: ${self.risk_threshold:.2f}
- Primary Risk Driver: {main_driver}
- Final Risk Score (0 - 10): {risk_score:.2f}
"""

        return risk_score, explanation.strip()
    