import pandas as pd

def extract_financial_data():
    """Extracts raw market data from the local data lake (CSV)."""
    file_path = '../data/raw/market_data_raw.csv'
    print(f"Extracting financial data from {file_path}...")
    
    df = pd.read_csv(file_path)
    print(f"Successfully extracted {len(df)} records.")
    return df

if __name__ == "__main__":
    raw_df = extract_financial_data()
    print("\n--- Raw Data Preview ---")
    print(raw_df.head())