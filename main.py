from src.extract import extract_financial_data
from src.transform import transform_data
from src.load import load_data

def run_pipeline():
    print("=== Starting Financial ETL Pipeline ===")
    
    # 1. Extract
    raw_df = extract_financial_data()
    
    # 2. Transform
    clean_df = transform_data(raw_df)
    
    # 3. Load
    load_data(clean_df, 'market_metrics')
    
    print("=== Pipeline Execution Complete ===")

if __name__ == "__main__":
    run_pipeline()