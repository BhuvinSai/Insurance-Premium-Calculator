import pandas as pd
import matplotlib.pyplot as plt
from risk_asses import RiskAssessmentEngine
from pricing_calcu import PricingCalculator
from market_analyzer import MarketAnalyzer


def visualize_results(results_df):

    # 1. AI Premium Distribution
    plt.figure()
    plt.hist(results_df['Final Premium'], bins=20)
    plt.title("AI Generated Premium Distribution")
    plt.xlabel("Premium Amount")
    plt.ylabel("Number of Customers")
    plt.show()

    # 2. Risk Score Distribution
    plt.figure()
    plt.hist(results_df['Risk Score'], bins=20)
    plt.title("Risk Score Distribution")
    plt.xlabel("Risk Score")
    plt.ylabel("Number of Customers")
    plt.show()

    # 3. Company Profit Distribution
    plt.figure()
    plt.hist(results_df['Profit'], bins=20)
    plt.title("Company Profit Distribution")
    plt.xlabel("Profit per Customer")
    plt.ylabel("Number of Customers")
    plt.show()

    # 4. Risk vs Premium Relationship
    plt.figure()
    plt.scatter(results_df['Risk Score'], results_df['Final Premium'])
    plt.title("Risk Score vs Final Premium")
    plt.xlabel("Risk Score")
    plt.ylabel("Final Premium")
    plt.show()


# ================= MAIN ORCHESTRATION =================

def main():

    print("\n================ TECHNOSHOPY AI INSURANCE SYSTEM ================\n")

    df = pd.read_csv("car_insurance_premium_dataset.csv")
    total_records = len(df)
    print(f"Dataset Loaded Successfully ✅ ({total_records} records)\n")

    # User Choice
    while True:
        try:
            n = int(input(f"Enter how many individuals you want to analyze (1 - {total_records}): "))
            if 1 <= n <= total_records:
                break
            else:
                print("Enter value within range.")
        except ValueError:
            print("Please enter a valid number.")

    print(f"\nProcessing {n} customers using AI system...\n")

    risk_engine = RiskAssessmentEngine()
    pricing_engine = PricingCalculator()
    market_engine = MarketAnalyzer()

    results = []

    for index, row in df.head(n).iterrows():

        applicant_data = {
            'Driver Age': row['Driver Age'],
            'Previous Accidents': row['Previous Accidents'],
            'Annual Mileage (x1000 km)': row['Annual Mileage (x1000 km)']
        }

        # ---- AI PIPELINE ----

        risk_score, risk_expl = risk_engine.calculate_risk_score(applicant_data)
        base_premium, pricing_expl = pricing_engine.calculate_base_premium(risk_score)
        final_premium, market_expl = market_engine.analyze_market_and_adjust(
            base_premium, applicant_data
        )

        profit = final_premium - row['Insurance Premium ($)']

        # Store results for visualization
        results.append({
            "Risk Score": risk_score,
            "Final Premium": final_premium,
            "Original Premium": row['Insurance Premium ($)'],
            "Profit": profit
        })

        # ---------- OUTPUT PER CUSTOMER ----------

        print(f"\n================ CUSTOMER #{index + 1} ================")
        print("Applicant Profile:")
        for k, v in applicant_data.items():
            print(f"{k}: {v}")

        print("\n--- Risk Assessment ---")
        print(risk_expl)

        print("\n--- Pricing Calculation ---")
        print(pricing_expl)

        print("\n--- Market Optimization ---")
        print(market_expl)

        print(f"\n✅ Final Premium: ${final_premium:.2f}")
        print(f"📈 Company Profit: ${profit:.2f}")
        print("====================================================")

    # ================= VISUAL ANALYTICS =================

    results_df = pd.DataFrame(results)

    print("\n📊 Generating Graphical Business Insights...")
    visualize_results(results_df)

    print("\n✅ Analysis Complete. System Ready for Evaluation.")


if __name__ == "__main__":
    main()
