import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

def generate_market_data():
    print("Generating mock financial data...")
    os.makedirs('../data/raw', exist_ok=True)
    
    tickers = ['AAPL', 'MSFT', 'EGP=X']
    dates = [datetime.today() - timedelta(days=x) for x in range(30)]
    all_data = []

    for ticker in tickers:
        # Set base prices
        if ticker == 'AAPL': base = 170.0
        elif ticker == 'MSFT': base = 400.0
        else: base = 47.0 # EGP exchange rate
        
        for date in dates:
            # Skip weekends to simulate real markets
            if date.weekday() >= 5 and ticker != 'EGP=X': 
                continue
                
            # Create realistic daily fluctuations
            daily_change = np.random.normal(0, base * 0.02)
            open_price = base + daily_change
            close_price = open_price + np.random.normal(0, base * 0.01)
            high_price = max(open_price, close_price) + abs(np.random.normal(0, base * 0.005))
            low_price = min(open_price, close_price) - abs(np.random.normal(0, base * 0.005))
            
            all_data.append({
                'Date': date.strftime('%Y-%m-%d'),
                'Open': round(open_price, 2),
                'Close': round(close_price, 2),
                'High': round(high_price, 2),
                'Low': round(low_price, 2),
                'Volume': int(np.random.uniform(1000000, 50000000) if ticker != 'EGP=X' else 0),
                'Symbol': ticker
            })
            base = close_price # update base for next day's simulation

    df = pd.DataFrame(all_data)
    
    # Sort by date and symbol
    df = df.sort_values(['Date', 'Symbol']).reset_index(drop=True)
    
    file_path = '../data/raw/market_data_raw.csv'
    df.to_csv(file_path, index=False)
    print(f"Successfully generated {len(df)} records to {file_path}")

if __name__ == "__main__":
    generate_market_data()