import pandas as pd
import os
from src.config import DATA_RAW_DIR, DATA_PROCESSED_DIR, RAW_DATA_FILE, PROCESSED_DATA_FILE

def load_data():
    """Load data from CSV."""
    file_path = os.path.join(DATA_RAW_DIR, RAW_DATA_FILE)
    try:
        df = pd.read_csv(file_path)
        print(f"Data loaded successfully with shape: {df.shape}")
        return df
    except FileNotFoundError:
        print("Error: Raw data file not found.")
        return pd.DataFrame()

def clean_and_feature_engineer(df):
    """
    Cleans data, aggregates to total daily sales, and generates features.
    Designed for 'store_sales.csv' structure (date, store, item, sales).
    """
    if df.empty:
        return df

    # 1. Convert date and sort
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')

    # 2. AGGREGATION: 
    # The CSV contains sales for multiple stores and items. 
    # We sum them up to get "Total Global Sales" per day for the model.
    daily = df.groupby('date')['sales'].sum().reset_index()

    # 3. Handle missing values (simple forward fill)
    daily['sales'] = daily['sales'].ffill()

    # 4. Feature Engineering
    daily['month'] = daily['date'].dt.month
    daily['day_of_week'] = daily['date'].dt.dayofweek
    daily['is_weekend'] = daily['day_of_week'].apply(lambda x: 1 if x >= 5 else 0)
    
    # Lag features (Previous day sales)
    daily['lag_1'] = daily['sales'].shift(1)
    daily['lag_2'] = daily['sales'].shift(2)
    
    # Rolling average
    daily['rolling_mean_3'] = daily['sales'].rolling(window=3).mean()

    # Drop NaNs created by lagging
    daily.dropna(inplace=True)
    
    print(f"Data processed. Final shape: {daily.shape}")
    return daily

def save_processed_data(df):
    os.makedirs(DATA_PROCESSED_DIR, exist_ok=True)
    file_path = os.path.join(DATA_PROCESSED_DIR, PROCESSED_DATA_FILE)
    df.to_csv(file_path, index=False)
    print(f"Processed data saved to {file_path}")

def run_pipeline():
    df = load_data()
    processed_df = clean_and_feature_engineer(df)
    save_processed_data(processed_df)
    return processed_df