import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, accuracy_score
import joblib

def train_and_save_rf_model():
    """
    Trains a Random Forest Classifier to predict customer conversion (Quote_Accepted)
    based on price difference and applicant risk features.
    Saves the trained model and scaler for use in the MarketAnalyzer.
    """
    # --- 1. Load Data ---
    try:
        # This file contains the synthetic 'Price_Difference' and 'Quote_Accepted' columns
        df = pd.read_csv('conversion_data.csv')
    except FileNotFoundError:
        print("Error: 'conversion_data.csv' not found. Please ensure the data generation step was run.")
        return

    # --- 2. Define Features and Target ---
    # The primary predictor is 'Price_Difference'. Risk factors (Age/Claims) are secondary features.
    FEATURES = ['Price_Difference', 'Driver Age', 'Previous Accidents'] 
    TARGET = 'Quote_Accepted'
    
    X = df[FEATURES]
    y = df[TARGET]

    # --- 3. Scaling ---
    # Standardize features (ensures consistency for deployment)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Save the fitted scaler object for production use
    joblib.dump(scaler, 'rf_conversion_scaler.pkl')
    print("StandardScaler saved to rf_conversion_scaler.pkl")

    # --- 4. Train the Random Forest Model ---
    print("Training Random Forest Classifier (Non-linear Optimization Model)...")
    # Random Forest is chosen for its high accuracy in modeling non-linear customer behavior.
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_scaled, y)

    # --- 5. Evaluate Model ---
    y_proba = rf_model.predict_proba(X_scaled)[:, 1]
    auc = roc_auc_score(y, y_proba)
    
    print(f"Random Forest Model (Conversion) trained successfully.")
    print(f"ROC AUC Score (Train Data): {auc:.4f}")

    # --- 6. Save the Trained Model ---
    joblib.dump(rf_model, 'rf_conversion_model.pkl')
    print("Trained Random Forest model saved to rf_conversion_model.pkl")


if __name__ == '__main__':
    train_and_save_rf_model()