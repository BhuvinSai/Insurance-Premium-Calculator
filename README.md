# Insurance-Premium-Calculator  
## Dynamic AI Insurance Premium System

[![Python Version](https://img.shields.io/badge/python-3.x-blue)](https://www.python.org/)  

---

## Overview
This repository contains a complete AI-driven Insurance Premium Calculation System that simulates real-world, personalized insurance pricing. The system integrates Machine Learning models, actuarial principles, and market optimization strategies to calculate risk-based premiums and generate actionable business insights.

The project demonstrates expertise in:  
- Artificial Intelligence & Machine Learning  
- Actuarial Critical Thinking  
- Data Analysis & Visualization  
- Modular Software Architecture (OOP)  

---

## Problem Statement & Solution Approach

### Challenge
Traditional insurance pricing methods are often manual, static, and do not dynamically adapt to customer profiles or fluctuating market conditions, leading to inefficient risk assessment and sub-optimal profitability.

### Solution
The system automates the complete pricing pipeline by combining the precision of ML models with rigorous actuarial logic and market simulation.

---

## Challenges Tackled

| Challenge | Solution Component | Skill Demonstrated |
|-----------|-----------------|-----------------|
| Customer Risk Assessment | RiskAssessmentEngine (GLM/Heuristic) | AI/ML – Predictive Modeling |
| Fair & Profitable Premium | PricingCalculator (Actuarial Formulas) | Critical Thinking – Actuarial Principles |
| Market Adjustment | MarketAnalyzer (Random Forest/Simulated Logic) | AI/ML Optimization & Business Logic |
| Scalable & Interactive Analysis | app.py (Streamlit Dashboard) | Data Visualization & BI |

---

## System Architecture & Components

The solution follows a professional insurance pricing pipeline:  
**Data → Risk Assessment → Premium Calculation → Market Optimization → Quote → Visual Analysis**

| Component | Python Class | Role | Skill Demonstrated |
|-----------|-------------|------|-----------------| 
| Risk Profiling | RiskAssessmentEngine | Converts driver data into a Risk Score (0–10) using a trained ML model or fallback heuristic | AI/ML – Predictive Modeling |
| Premium Calculation | PricingCalculator | Converts Risk Score into Base Premium using actuarial constants (Cost + Profit + Fees) | Actuarial Principles |
| Market Adjustment | MarketAnalyzer | Optimizes final premium using a Random Forest model or simulated market rules | AI/ML Optimization & Business Logic |
| Dashboard | app.py (Streamlit) | Interactive analysis and visualizations | Data Visualization & BI |
| Orchestration | main_orches.py | CLI-based batch processing of the customer dataset | Modular Architecture |

---

## Project Structure

techsophy/
├── ```src/ # Python source code```


│ ├── ```app.py # Streamlit dashboard interface```


│ ├── risk_asses.py # RiskAssessmentEngine class
│ ├── pricing_calcu.py # PricingCalculator class
│ └── market_analyzer.py # MarketAnalyzer class
├── data_and_model/ # Dataset and ML models
│ ├── car_insurance_premium_dataset_TEST.csv
│ ├── glm_risk_model.pkl
│ ├── risk_scaler.pkl
│ ├── rf_conversion_model.pkl
│ └── rf_conversion_scaler.pkl
└── README.md # Project documentation

---

## Prerequisites

- Python 3.x installed  
- Required Python libraries:  

```bash
pip install streamlit pandas numpy joblib scikit-learn
```
---
How to Run the Application
1. CLI Mode (Batch Processing)


Run the pipeline in batch mode from your terminal:

```bash
python src/main_orches.py
```

Action: Enter the number of customers to analyze when prompted.

Output: View the calculated risk, premium, market adjustment, and profit results in the terminal.

2. Streamlit Dashboard (Interactive Analysis)

Launch the interactive dashboard in your web browser:
```bash
streamlit run src/app.py
```

Action: Select the number of customers to analyze using the sidebar controls.

Output: View the calculated metrics, dataset, and interactive charts for business insights.

Business Value

This system simulates the core operations of a modern insurance carrier, demonstrating the ability to:

Assess customer risk dynamically using data and AI.

Optimize pricing based on both risk profile and market conditions.

Maintain profitability while ensuring fair pricing.

It serves as an enterprise-ready demonstration of an AI-driven pricing solution.

Author

Bhuvin Sai
