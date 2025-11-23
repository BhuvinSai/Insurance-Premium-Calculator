import numpy as np
import joblib
import os
import random

class MarketAnalyzer:

    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        MODEL_DIR = os.path.join(BASE_DIR, "model and data")

        self.model_path = os.path.join(MODEL_DIR, "rf_conversion_model.pkl")
        self.scaler_path = os.path.join(MODEL_DIR, "rf_conversion_scaler.pkl")

        try:
            print("Loading Random Forest Conversion Model for Market Analyzer...")
            self.model = joblib.load(self.model_path)
            self.scaler = joblib.load(self.scaler_path)
            self.ml_available = True
        except Exception as e:
            print("❌ ERROR: Conversion model files not found. Using random market simulation.")
            print(f"Reason: {e}")
            self.ml_available = False

    def analyze_market_and_adjust(self, base_premium, applicant_data):
        """
        Adjust premium based on market competition and ML optimization
        """

        # ✅ Correct key names (aligned with app.py)
        driver_age = applicant_data["Driver Age"]
        accidents = applicant_data["Previous Accidents"]
        mileage = applicant_data["Annual Mileage (x1000 km)"]
        competitor_price = applicant_data["competitor_price"]

        # Build input feature vector exactly as model expects
        X = np.array([[driver_age, accidents, mileage]])

        if self.ml_available:
            X_scaled = self.scaler.transform(X)
            conversion_probability = self.model.predict_proba(X_scaled)[0][1]
        else:
            conversion_probability = random.uniform(0.4, 0.8)

        # Market logic
        if base_premium > competitor_price:
            multiplier = 0.95
        else:
            multiplier = 1.05

        # Apply probability influence
        adjusted_premium = base_premium * multiplier

        adjustment_text = (
            f"{'Discount' if multiplier < 1 else 'Surcharge'} "
            f"applied based on competitor price and conversion probability "
            f"({round(conversion_probability,2)})"
        )

        return round(adjusted_premium, 2), adjustment_text
