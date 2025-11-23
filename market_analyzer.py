import random
from typing import Tuple, Dict, Any
import joblib
import numpy as np
import warnings # <-- NEW: Import warnings module

# --- Market Analyzer Module (OOP) ---
# Implements the Market Adjustment Step (Pricing Optimization) using a trained ML model.

class MarketAnalyzer:
    """
    Adjusts the base premium based on strategic pricing optimization guided by a 
    Random Forest Conversion Model (AI/ML).
    """
    
    # Regulatory and Profit Guardrails (Critical Thinking)
    MIN_PROFIT_MULTIPLIER: float = 0.90
    MAX_SURCHARGE_MULTIPLIER: float = 1.10
    
    # Features the Conversion Model expects
    MODEL_FEATURES: list = ['Price_Difference', 'Driver Age', 'Previous Accidents'] 

    def __init__(self):
        """Initializes the analyzer by loading the trained model and scaler."""
        print("Loading Random Forest Conversion Model for Market Analyzer...")
        try:
            self.model = joblib.load('rf_conversion_model.pkl')
            self.scaler = joblib.load('rf_conversion_scaler.pkl')
        except FileNotFoundError:
            print("ERROR: Conversion model files not found. Using random market simulation.")
            self.model = None

    def analyze_market_and_adjust(self, base_premium: float, applicant_data: dict) -> Tuple[float, str]:
        """
        Determines the final premium by optimizing the adjustment multiplier (0.90 - 1.10)
        to maximize expected revenue using the trained conversion model.
        """
        
        # --- 1. Define Optimization Space and Baseline ---
        multipliers = np.linspace(self.MIN_PROFIT_MULTIPLIER, self.MAX_SURCHARGE_MULTIPLIER, 21)
        np.random.seed(int(base_premium * 100))
        simulated_competitor_price = base_premium * random.uniform(0.98, 1.02)
        
        best_expected_profit = -np.inf
        optimal_multiplier = 1.0
        
        # --- 2. Iterate and Optimize (AI/ML Decision Loop) ---
        for multiplier in multipliers:
            quoted_premium = base_premium * multiplier
            price_difference = quoted_premium - simulated_competitor_price
            
            input_data = np.array([[
                price_difference, 
                applicant_data.get('Driver Age', 30),
                applicant_data.get('Previous Accidents', 0)
            ]])
            
            # Predict Conversion Probability (ML Core)
            if self.model is None:
                conversion_prob = 1.0 if price_difference < 0 else 0.5
            else:
                # --- WARNING SUPPRESSION APPLIED HERE ---
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore")
                    scaled_data = self.scaler.transform(input_data)
                    conversion_prob = self.model.predict_proba(scaled_data)[0][1] 

            profit_margin = quoted_premium - base_premium 
            expected_profit = conversion_prob * profit_margin
            
            if expected_profit > best_expected_profit:
                best_expected_profit = expected_profit
                optimal_multiplier = multiplier

        # --- 3. Final Calculation and Explanation ---
        final_multiplier = optimal_multiplier
        final_premium = base_premium * final_multiplier
        adjustment_amount = final_premium - base_premium
        adjustment_percentage = (final_multiplier - 1.0) * 100
            
        explanation = f"""
[C] Market Adjustment Details (Dynamic Pricing Optimization - AI/ML):
        - **Optimization Goal:** Maximize Expected Profit per Quote ($\mathrm{{P}}(\text{{Conversion}}) \times \text{{Profit}}$).
        - **Simulated Competitor Price:** $\${simulated_competitor_price:.2f}$
        - **Predicted Optimal Multiplier:** {final_multiplier:.2f}
        - **Calculated Expected Profit:** $\${best_expected_profit:.2f}$
        - **Adjustment Applied:** {adjustment_percentage:+.2f}\% (Amount: $\${adjustment_amount:+.2f}$)
        - **Final Price Quoted:** $\${final_premium:.2f}$
        """

        return final_premium, explanation.strip()


if __name__ == '__main__':
    # REMOVED VERBOSE TEST OUTPUT block here to prevent clutter in your main execution.
    pass