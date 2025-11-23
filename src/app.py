import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="sklearn")
import streamlit as st
import pandas as pd
import os

from risk_asses import RiskAssessmentEngine
from pricing_calcu import PricingCalculator
from market_analyzer import MarketAnalyzer

# ---------------- PATH CONFIG ----------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "model and data")
DATA_PATH = os.path.join(DATA_DIR, "car_insurance_premium_dataset_TEST.csv")

# ---------------- LOAD DATA ----------------
try:
    data = pd.read_csv(DATA_PATH)
except:
    st.error("Dataset not found. Check path or filename.")
    st.stop()

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Insurance Premium System", layout="wide")
st.title("🚗 AI-Powered Insurance Premium Dashboard")
st.markdown("ML-based system for risk assessment, premium pricing, and market optimization.")

# ---------------- SIDEBAR INPUT ----------------
st.sidebar.header("Analysis Settings")
num_customers = st.sidebar.slider(
    "How many customers to analyze?",
    1, len(data), 5
)

# ---------------- ENGINES ----------------
risk_engine = RiskAssessmentEngine()
pricing_engine = PricingCalculator()
market_engine = MarketAnalyzer()

# ---------------- DATA PREP ----------------
subset = data.head(num_customers).copy()

# Ensure the columns match what the scaler expects
expected_features = ["Driver Age", "Previous Accidents", "Annual Mileage (x1000 km)"]
for col in expected_features:
    if col not in subset.columns:
        if col == "Driver Age":
            subset[col] = 30
        elif col == "Previous Accidents":
            subset[col] = 0
        elif col == "Annual Mileage (x1000 km)":
            subset[col] = 10

# ---------------- CALCULATE RISK AND PREMIUM ----------------
def compute_risk(row):
    # Convert row to dict for RiskAssessmentEngine
    data_dict = {
        "Driver Age": row.get("Driver Age", 30),
        "Previous Accidents": row.get("Previous Accidents", 0),
        "Annual Mileage (x1000 km)": row.get("Annual Mileage (x1000 km)", 10)
    }
    return risk_engine.calculate_risk(data_dict)

def compute_premium(risk_score):
    return pricing_engine.calculate_premium(risk_score)

# Compute RiskScore and PremiumAmount
subset["RiskScore"] = subset.apply(lambda row: compute_risk(row), axis=1)
subset["PremiumAmount"] = subset["RiskScore"].apply(compute_premium)

# ---------------- DISPLAY DATA ----------------
st.header("📈 Dataset Analysis")
st.dataframe(subset)

# ---------------- VISUALIZATIONS ----------------
st.subheader("Premium Distribution")
st.bar_chart(subset["PremiumAmount"])

st.subheader("Risk vs Premium Trend")
st.line_chart(subset[["RiskScore", "PremiumAmount"]])

st.subheader("Company Profit Estimation")
subset["Estimated_Profit"] = subset["PremiumAmount"] * 0.25
st.bar_chart(subset["Estimated_Profit"])
