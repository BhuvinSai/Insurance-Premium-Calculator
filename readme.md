Dynamic Insurance Premium Calculator

Overview

This repository contains a modular Python application designed to calculate personalized insurance premiums. The system uses Object-Oriented Programming (OOP) to separate the calculation logic into distinct modules, demonstrating skills in AI/ML simulation, Actuarial Critical Thinking, and Software Architecture.

The premium is dynamically calculated based on individual risk factors and simulated market trends.

Architectural Compliance (Skills Demonstrated)

The solution strictly follows the required architecture: Data --> Risk --> Pricing --> Market -->Quote.

Component

Python Class

Role

Skill Demonstrated

Risk Profiling

RiskAssessmentEngine

Converts driver data (age, claims, mileage) into a quantitative Risk Score (0-10).

AI/ML (Predictive Modeling: Predicting Loss Frequency/Severity)

Premium Calculation

PricingCalculator

Converts the Risk Score into a Base Premium using actuarial constants (Cost + Profit + Fees).

Critical Thinking (Actuarial Principles)

Market Adjustment

MarketAnalyzer

Applies a final discount/surcharge based on simulated real-time market trends, balancing profit vs. competition.

AI/ML (Pricing Optimization) & Critical Thinking (Regulatory Constraints)

Quote Generation

main.py

Orchestrates the entire flow using class instances and provides a detailed Explanation of the final price.

Clear Architecture & Modular Structure

Running the Application

Prerequisites

You must have Python installed. This project uses only standard Python libraries.

Installation & Execution

Place all seven files (.py and .txt/.md) into a single folder.

Navigate to that folder in your terminal.

Run the main application: python main.py