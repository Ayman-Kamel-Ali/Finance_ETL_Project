# Automated Financial Market Data Pipeline

## 📌 The Business Problem

Financial analysts need to track daily stock prices and currency exchange rates to advise clients, but manually pulling this data and calculating trends across different assets is time-consuming and prone to human error.

## 💡 The Solution

I built an automated Python ETL pipeline that ingests daily market data (simulating an external REST API connection), cleans the time-series data, and calculates critical business metrics including the 7-Day Moving Average and Daily Volatility. The clean data is securely loaded into a PostgreSQL database, secured with environment configuration files.

## 🛠️ Tech Stack

* **Language:** Python (Pandas, NumPy)
* **Database:** PostgreSQL, SQLAlchemy
* **Architecture:** Modular ETL, Configuration Management (YAML)
* **Concepts:** Time-series data manipulation, financial metric calculation, defensive programming

## 📊 Business Outcomes

* **Automated Technical Analysis:** Automatically calculates Moving Averages and Volatility so analysts can focus on strategy rather than data entry.
* **Robust Error Handling:** Built with defensive programming to handle API rate limits and missing weekend market data.
* **Secure Architecture:** Implemented `.gitignore` and YAML config files to ensure database credentials are never exposed in source control.

## 🚀 How to Run Locally

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Generate the mock market data: `python src/generate_mock_market_data.py`
4. Execute the pipeline: `python main.py`
