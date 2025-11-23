# Insurance-Premium-Calculator  
## Dynamic AI Insurance Premium System

[![Python Version](https://img.shields.io/badge/python-3.x-blue)](https://www.python.org/)  

---

## Overview
This repository contains a **comprehensive AI-driven Insurance Premium Calculation System** designed to simulate real-world, personalized insurance pricing. The system integrates advanced Machine Learning models, actuarial methodologies, and market optimization strategies to calculate risk-adjusted insurance premiums. It provides both technical and business-level insights, enabling insurance carriers to make informed, data-driven decisions.

The platform demonstrates practical expertise in several key domains:  
- **Artificial Intelligence & Machine Learning** – for predicting individual risk and automating pricing decisions.  
- **Actuarial Critical Thinking** – applying domain knowledge and actuarial formulas to calculate fair and profitable premiums.  
- **Data Analysis & Visualization** – transforming raw customer and market data into actionable insights through dashboards and charts.  
- **Modular Software Architecture (OOP)** – ensuring code maintainability, scalability, and reusability across multiple modules.

This project serves as a real-world example of bridging **data science** with **business analytics** in the insurance domain, showcasing how AI can enhance operational efficiency, customer fairness, and profitability.

---

## Problem Statement & Solution Approach

### Challenge
Traditional insurance pricing methods are often **manual, static, and reactive**, relying heavily on historical data and actuarial judgment without dynamically adapting to individual customer profiles or evolving market conditions. This leads to several inefficiencies, including:  

- Mispriced premiums that may overcharge or undercharge customers.  
- Suboptimal risk assessment, potentially resulting in higher loss ratios.  
- Lack of real-time insights into market and portfolio performance.  

These challenges highlight the need for a **dynamic and data-driven solution** that can automate risk assessment, premium calculation, and market adjustment processes.

### Solution
Our system addresses these challenges by **automating the complete insurance pricing pipeline**:  

1. **Data Ingestion & Preprocessing** – Customer profiles, driving history, and market data are cleaned, normalized, and prepared for modeling.  
2. **Risk Assessment** – Using Machine Learning models (GLM and Random Forest) and fallback heuristics, the system evaluates each customer's risk profile.  
3. **Premium Calculation** – The risk scores are converted into base premiums using actuarial formulas that account for cost, profit, and fees.  
4. **Market Adjustment** – Premiums are optimized based on simulated market scenarios, competitor analysis, and regulatory constraints.  
5. **Interactive Reporting** – The calculated metrics are visualized in a Streamlit dashboard, enabling interactive exploration of the portfolio and customer insights.  

This approach ensures **accurate, fair, and profitable insurance pricing**, reducing manual workload while providing actionable insights for business strategy.

---

## Challenges Tackled

| Challenge | Solution Component | Skill Demonstrated |  
|-----------|-----------------|-----------------|  
| Customer Risk Assessment | RiskAssessmentEngine (GLM/Heuristic) | AI/ML – Predictive Modeling; accurately classifies customers into risk bands based on historical and simulated data. |  
| Fair & Profitable Premium | PricingCalculator (Actuarial Formulas) | Combines risk scores with actuarial principles to produce fair yet profitable premiums. |  
| Market Adjustment | MarketAnalyzer (Random Forest/Simulated Logic) | Adjusts premiums dynamically based on competitor rates, market trends, and profitability thresholds. |  
| Scalable & Interactive Analysis | app.py (Streamlit Dashboard) | Provides interactive visualization for decision-making and strategic analysis. |

Each component demonstrates **a combination of domain knowledge, technical skill, and software engineering best practices**, making the solution both robust and enterprise-ready.

---

## System Architecture & Components

The solution follows a **modular pipeline architecture**:

**Data → Risk Assessment → Premium Calculation → Market Optimization → Quote Generation → Interactive Visualization**

| Component | Python Class | Role | Skill Demonstrated |  
|-----------|-------------|------|-----------------|  
| Risk Profiling | RiskAssessmentEngine | Converts customer data into a **risk score (0–10)** using ML models or fallback heuristics for missing data. This score quantifies the probability of claims and potential loss. | AI/ML – Predictive Modeling & Data Science |  
| Premium Calculation | PricingCalculator | Converts risk scores into **base insurance premiums** using actuarial formulas including cost of coverage, profit margin, and operational fees. | Actuarial Principles & Critical Thinking |  
| Market Adjustment | MarketAnalyzer | Optimizes final premiums using Random Forest predictions or simulated market rules to balance competitiveness and profitability. | AI/ML Optimization & Business Logic |  
| Dashboard | app.py (Streamlit) | Provides **interactive charts, tables, and KPI visualization** for portfolio analysis and business insights. | Data Visualization & Business Intelligence |  
| Orchestration | main_orches.py | Enables **batch processing** for multiple customers through CLI, automating the full risk and pricing workflow. | Modular Architecture & Automation |

This **modular approach** allows each component to be tested, reused, or enhanced independently while maintaining a **cohesive end-to-end system**.

---

## Project Structure

techsophy/  
├── `src/` # Python source code  
│   ├── `app.py` # Streamlit dashboard interface  
│   ├── `risk_asses.py` # RiskAssessmentEngine class  
│   ├── `pricing_calcu.py` # PricingCalculator class  
│   └── `market_analyzer.py` # MarketAnalyzer class  

├── `data_and_model/` # Dataset and ML models  
│   ├── `car_insurance_premium_dataset_TEST.csv`  
│   ├── `car_insurance_premium_dataset.csv`  
│   ├── `glm_risk_model.pkl`  
│   ├── `risk_scaler.pkl`  
│   ├── `rf_conversion_model.pkl`  
│   └── `rf_conversion_scaler.pkl`  

└── `README.md` # Project documentation  

> **Note:** The `data_and_model` folder contains both the sample dataset for testing and the pre-trained models used in the system.  

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
