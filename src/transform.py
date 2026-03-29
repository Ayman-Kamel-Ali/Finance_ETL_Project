import pandas as pd
from src.extract import extract_financial_data

def transform_data(df):
    """Calculates financial metrics like Moving Averages and Volatility."""
    print("Starting data transformation...")
    
    # Ensure data is sorted chronologically for accurate rolling calculations
    df = df.sort_values(['Symbol', 'Date'])
    
    # 1. Calculate 7-Day Moving Average for the Closing Price
    df['7_Day_MA'] = df.groupby('Symbol')['Close'].transform(
        lambda x: x.rolling(window=7, min_periods=1).mean().round(2)
    )
    
    # 2. Calculate Daily Volatility (High - Low)
    df['Daily_Volatility'] = (df['High'] - df['Low']).round(2)
    
    print(f"Transformation complete. Added business metrics for {len(df)} records.")
    return df

if __name__ == "__main__":
    raw_df = extract_financial_data()
    clean_df = transform_data(raw_df)
    
    print("\n--- Transformed Data Preview ---")
    print(clean_df.head(10))