import pandas as pd
import os

def extract_financial_data():
    """Extracts raw market data from the local data lake (CSV)."""
    
    # Dynamically build the correct path no matter where the script is run from
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, '..', 'data', 'raw', 'market_data_raw.csv')
    
    # Normalize the path to make it look clean on Windows (optional but nice)
    file_path = os.path.normpath(file_path)
    
    print(f"Extracting financial data from {file_path}...")
    
    df = pd.read_csv(file_path)
    print(f"Successfully extracted {len(df)} records.")
    return df

if __name__ == "__main__":
    raw_df = extract_financial_data()
    print("\n--- Raw Data Preview ---")
    print(raw_df.head())