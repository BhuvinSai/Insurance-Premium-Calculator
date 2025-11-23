# Dynamic AI Insurance Premium System

## Overview

This repository contains a complete **AI-driven Insurance Premium Calculation System** designed to simulate a real-world insurance pricing pipeline. The system calculates personalized insurance premiums using Machine Learning models, actuarial logic, and market optimization strategies.

The project demonstrates strong skills in:

* Artificial Intelligence & Machine Learning
* Actuarial Critical Thinking
* Data Analysis & Visualization
* Modular Software Architecture (OOP)

The premium is calculated dynamically based on customer risk profile and simulated market behavior, and the system also provides **graphical insights** to evaluate business profitability and customer risk distribution.

---

## System Architecture (Pipeline)

The solution strictly follows the professional insurance architecture:

```
Data → Risk → Pricing → Market → Quote → Visual Analysis
```

---

## Components & Responsibilities

| Component           | Python Class         | Role                                                                                        | Skill Demonstrated                       |
| ------------------- | -------------------- | ------------------------------------------------------------------------------------------- | ---------------------------------------- |
| Risk Profiling      | RiskAssessmentEngine | Converts driver data into a Risk Score (0–10) using a trained Logistic Regression ML model. | AI/ML – Predictive Modeling              |
| Premium Calculation | PricingCalculator    | Converts Risk Score into Base Premium using actuarial constants (Cost + Profit + Fees).     | Critical Thinking – Actuarial Principles |
| Market Adjustment   | MarketAnalyzer       | Optimizes final premium using Random Forest model + regulatory constraints.                 | AI/ML Optimization & Business Logic      |
| Quote Orchestration | main_orches.py       | Controls data flow, integrates modules, and generates final insurance quote.                | Modular Architecture                     |
| Data Analysis       | Visualization Module | Generates graphs for premium, risk, and profitability insights.                             | Business Intelligence & Analytics        |

---

## Machine Learning Integration

This system uses pre-trained ML models stored as:

* `glm_risk_model.pkl` → Logistic Regression for Risk Prediction
* `rf_conversion_model.pkl` → Random Forest for Market Optimization

The dataset (`car_insurance_premium_dataset.csv`) is used as testing input and is processed record-by-record through the AI pipeline.

The project separates:

* Training Phase (offline using dataset)
* Inference Phase (real-time prediction using saved models)

This reflects industry-standard ML architecture.

---

## Visual Analytics

The system automatically generates the following charts:

1. **AI Premium Distribution** – Shows how premiums are spread across customers.
2. **Risk Score Distribution** – Displays customer risk segmentation.
3. **Profit Distribution** – Evaluates company profitability per customer.
4. **Risk vs Premium Scatter Plot** – Validates fairness of risk-based pricing.

These visualizations allow analysis of:

* Business sustainability
* Model fairness
* Financial feasibility
* Risk exposure

---

## Features

✅ ML-based risk scoring
✅ Dynamic premium optimization
✅ Dataset-driven predictions
✅ User-selected number of customers to analyze
✅ Graphical business insights
✅ Profitability evaluation
✅ Clean professional output

---

## Project Structure

```
technoshopy-insurance-system/
│
├── main_orches.py
├── risk_asses.py
├── pricing_calcu.py
├── market_analyzer.py
├── car_insurance_premium_dataset.csv
├── glm_risk_model.pkl
├── rf_conversion_model.pkl
├── risk_scaler.pkl
├── rf_conversion_scaler.pkl
└── README.md
```

---

## How to Run the Application

### Prerequisites

* Python 3.x installed
* Required libraries:

```
pip install pandas matplotlib joblib scikit-learn
```

### Execution Steps

1. Place all project files in one folder.
2. Open terminal in that folder.
3. Run the application:

```
python main_orches.py
```

4. Enter how many customer records you want to analyze.
5. View:

   * Detailed output per customer
   * Automated graphical analysis

---

## Sample Output

* Risk Score Calculation
* Base Premium Calculation
* Market Adjusted Premium
* Company Profit Per Customer
* Graphical Insights

---

## Business Value

This system simulates how insurance companies:

* Assess customer risk
* Adjust premiums dynamically
* Maintain profitability
* Ensure fair pricing

It bridges **AI decision-making** with **business strategy**, making it an enterprise-ready solution.

---

## Author

Bhuvin Sai


---

## GitHub Repository

Provide this link during submission:

```
https://github.com/BhuvinSai/Insurance-Premium-Calculator

