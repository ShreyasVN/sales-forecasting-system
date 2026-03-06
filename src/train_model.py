import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib
from src.config import DATA_PROCESSED_DIR, MODEL_DIR, PREDICTION_FILE, MODEL_FILE, TEST_SIZE

def train_and_predict(df):
    # Define features and target
    # Exclude 'date' for training, keep it for final output alignment
    feature_cols = ['month', 'day_of_week', 'is_weekend', 'lag_1', 'lag_2', 'rolling_mean_3']
    target_col = 'sales'

    X = df[feature_cols]
    y = df[target_col]

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=TEST_SIZE, shuffle=False)
    
    # Train Model (Random Forest used for robustness)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate
    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    print(f"Model Training Complete. MAE: {mae:.2f}")

    # Save Model
    os.makedirs(MODEL_DIR, exist_ok=True)
    model_path = os.path.join(MODEL_DIR, MODEL_FILE)
    joblib.dump(model, model_path)

    # Generate Future Forecasts (Simulated)
    # In production, you would append future dates to the dataframe logic
    # Here we save the test predictions + actuals for Power BI visualization
    
    output_df = X_test.copy()
    output_df['actual_sales'] = y_test
    output_df['predicted_sales'] = predictions
    output_df['date'] = df.loc[y_test.index, 'date'] # Align dates

    # Save for Power BI
    pred_path = os.path.join(DATA_PROCESSED_DIR, PREDICTION_FILE)
    output_df.to_csv(pred_path, index=False)
    print(f"Predictions saved for Power BI at {pred_path}")

    return model