from src.data_processing import run_pipeline
from src.train_model import train_and_predict

def main():
    print("Starting Sales Analytics Pipeline...")
    
    # 1. Process Data
    processed_data = run_pipeline()
    
    if not processed_data.empty:
        # 2. Train Model and Forecast
        train_and_predict(processed_data)
        print("Pipeline completed successfully.")
    else:
        print("Pipeline halted due to data issues.")

if __name__ == "__main__":
    main()