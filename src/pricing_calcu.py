import numpy as np

class PricingCalculator:
    """
    Pricing Calculator uses actuarial logic to convert Risk Score into
    an insurance premium. This reflects realistic insurance pricing structure.

    Components:
    - Pure Risk Cost
    - Expense Loading
    - Profit Margin
    - Regulatory Safety Buffer
    """

    def __init__(self):
        # Base cost to cover administrative expenses
        self.fixed_base_cost = 3500  

        # Actuarial multipliers
        self.risk_weight = 1100
        self.expense_ratio = 0.15      # 15% operational expenses
        self.profit_margin = 0.20      # 20% profit target
        self.safety_buffer = 0.05      # 5% regulatory buffer

    def calculate_premium(self, risk_score):
        """
        Convert risk score into premium using actuarial formula
        """

        # 1. Pure Risk Premium (based on predicted risk)
        pure_risk_premium = self.fixed_base_cost + (risk_score * self.risk_weight)

        # 2. Expense Loading
        expense_cost = pure_risk_premium * self.expense_ratio

        # 3. Profit Margin
        profit_cost = pure_risk_premium * self.profit_margin

        # 4. Regulatory Buffer
        buffer_cost = pure_risk_premium * self.safety_buffer

        # 5. Final Premium
        final_premium = pure_risk_premium + expense_cost + profit_cost + buffer_cost

        return round(final_premium, 2)


    def breakdown(self, risk_score):
        """
        Explain premium components (useful for dashboard or reports)
        """

        pure_risk = self.fixed_base_cost + (risk_score * self.risk_weight)
        expenses = pure_risk * self.expense_ratio
        profit = pure_risk * self.profit_margin
        buffer = pure_risk * self.safety_buffer

        return {
            "Pure Risk Premium": round(pure_risk, 2),
            "Expenses": round(expenses, 2),
            "Profit Margin": round(profit, 2),
            "Safety Buffer": round(buffer, 2),
            "Total Premium": round(pure_risk + expenses + profit + buffer, 2)
        }
