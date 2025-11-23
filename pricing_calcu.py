from typing import Tuple

# --- Pricing Calculator Module (OOP) ---
# Converts Risk Score into Base Premium

class PricingCalculator:

    BASE_COST_PER_UNIT_RISK: float = 550.0
    FIXED_ADMIN_FEE: float = 150.0
    PROFIT_MARGIN_RATE: float = 0.15

    def calculate_base_premium(self, risk_score: float) -> Tuple[float, str]:

        pure_risk_cost = risk_score * self.BASE_COST_PER_UNIT_RISK
        profit_loading = pure_risk_cost * self.PROFIT_MARGIN_RATE
        gross_base_premium = pure_risk_cost + profit_loading + self.FIXED_ADMIN_FEE

        explanation = f"""
Pricing Calculation Details (Actuarial Logic):
- Risk Score Used: {risk_score:.2f}
- Pure Risk Cost: ${pure_risk_cost:.2f}
- Profit Margin (15%): +${profit_loading:.2f}
- Fixed Admin Fee: +${self.FIXED_ADMIN_FEE:.2f}
- Base Premium (Before Market Adjustment): ${gross_base_premium:.2f}
"""

        return gross_base_premium, explanation.strip()
