import os

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_RAW_DIR = os.path.join(BASE_DIR, 'data', 'raw')
DATA_PROCESSED_DIR = os.path.join(BASE_DIR, 'data', 'processed')
MODEL_DIR = os.path.join(BASE_DIR, 'models')

# File Names
# UPDATED: Points to the store_sales.csv dataset
RAW_DATA_FILE = 'store_sales.csv' 
PROCESSED_DATA_FILE = 'processed_features.csv'
PREDICTION_FILE = 'sales_predictions.csv'
MODEL_FILE = 'sales_model.pkl'

# Model Parameters
TEST_SIZE = 0.2
RANDOM_STATE = 42