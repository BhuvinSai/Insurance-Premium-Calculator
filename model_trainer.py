import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, accuracy_score
import joblib
import numpy as np

def train_and_save_risk_model(train_file, test_file, model_filename='glm_risk_model.pkl', scaler_filename='risk_scaler.pkl'):
    # --- 1. Load Data ---
    try:
        df_train = pd.read_csv(train_file)
        df_test = pd.read_csv(test_file)
    except FileNotFoundError:
        print("Error: Training or testing data file not found.")
        return

    TARGET = 'Insurance Premium ($)'
    FEATURES = ['Driver Age', 'Previous Accidents', 'Annual Mileage (x1000 km)']
    
    # --- 2. Define Target Threshold (Median of Training Data) ---
    median_premium = df_train[TARGET].median()
    print(f"Risk threshold (Median Premium) calculated from training data: {median_premium:.2f}")

    # Create binary target variable (High Risk = 1 if premium > median, 0 otherwise)
    df_train['Risk_Level'] = (df_train[TARGET] > median_premium).astype(int)
    df_test['Risk_Level'] = (df_test[TARGET] > median_premium).astype(int)

    # --- 3. Prepare Features and Scaling ---
    X_train = df_train[FEATURES]
    y_train = df_train['Risk_Level']
    X_test = df_test[FEATURES]
    y_test = df_test['Risk_Level']

    # Standardize features (Crucial for Logistic Regression/GLM)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Save the fitted scaler object for production use
    joblib.dump(scaler, scaler_filename)
    print(f"StandardScaler saved to {scaler_filename}")

    # --- 4. Train the Logistic Regression Model (GLM) ---
    print("Training Logistic Regression Model (GLM)...")
    glm_model = LogisticRegression(random_state=42)
    glm_model.fit(X_train_scaled, y_train)

    # --- 5. Evaluate Model on Test Set ---
    y_proba_test = glm_model.predict_proba(X_test_scaled)[:, 1]
    accuracy = accuracy_score(y_test, glm_model.predict(X_test_scaled))
    roc_auc = roc_auc_score(y_test, y_proba_test)
    
    print("\nModel Evaluation on Test Data:")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"ROC AUC: {roc_auc:.4f}")

    # --- 6. Save the Trained Model and Threshold ---
    joblib.dump(glm_model, model_filename)
    print(f"Trained GLM model saved to {model_filename}")
    np.save('risk_threshold.npy', median_premium)
    print("Median risk threshold saved to risk_threshold.npy")


if __name__ == '__main__':
    train_and_save_risk_model(
        train_file='car_insurance_premium_dataset.csv',
        test_file='car_insurance_premium_dataset_TEST.csv'
    )