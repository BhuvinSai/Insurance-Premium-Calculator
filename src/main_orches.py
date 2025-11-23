import os
import pandas as pd
from risk_asses import RiskAssessmentEngine
from pricing_calcu import PricingCalculator
from market_analyzer import MarketAnalyzer

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_PATH = os.path.join(BASE_DIR, "model and data", "car_insurance_premium_dataset.csv")

def main():

    print("\n======= TECHNOSHOPY AI INSURANCE SYSTEM =======\n")

    data = pd.read_csv(DATA_PATH)
    n = int(input("Enter number of customers to analyze: "))
    selected = data.head(n)

    risk_engine = RiskAssessmentEngine()
    pricing_engine = PricingCalculator()
    market_engine = MarketAnalyzer()

    for idx, row in selected.iterrows():

        applicant_data = {
            'Driver Age': row['Driver Age'],
            'Previous Accidents': row['Previous Accidents'],
            'Annual Mileage (x1000 km)': row['Annual Mileage (x1000 km)']
        }

        risk_score, risk_exp = risk_engine.calculate_risk_score(applicant_data)
        base_premium, price_exp = pricing_engine.calculate_base_premium(risk_score)
        final_premium, market_exp = market_engine.analyze_market_and_adjust(base_premium, applicant_data)

        print("\n---------------- CUSTOMER ----------------")
        print(applicant_data)
        print(risk_exp)
        print(price_exp)
        print(market_exp)
        print(f"FINAL PREMIUM: ${final_premium:.2f}")

if __name__ == "__main__":
    main()
