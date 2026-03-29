import pandas as pd
from sqlalchemy import create_engine, text
import yaml
import os

def load_config():
    """Loads database credentials from the config.yaml file."""
    # Build the absolute path to the config file
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config.yaml')
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

def create_db_if_not_exists(creds):
    """Connects to the default database to create the target database if it is missing."""
    default_engine = create_engine(
        f"postgresql://{creds['username']}:{creds['password']}@{creds['host']}:{creds['port']}/postgres", 
        isolation_level='AUTOCOMMIT'
    )
    
    with default_engine.connect() as conn:
        result = conn.execute(text(f"SELECT 1 FROM pg_database WHERE datname = '{creds['db_name']}'"))
        if not result.fetchone():
            print(f"Database '{creds['db_name']}' not found. Creating it automatically...")
            conn.execute(text(f"CREATE DATABASE {creds['db_name']}"))
        else:
            print(f"Database '{creds['db_name']}' already exists.")
            
    default_engine.dispose()

def load_data(df, table_name):
    """Loads transformed data into the PostgreSQL database using secure credentials."""
    # 1. Load the credentials dictionary
    config = load_config()
    creds = config['database']
    
    # 2. Ensure database exists
    create_db_if_not_exists(creds)
    
    # 3. Connect and load
    print(f"Loading {len(df)} records into '{table_name}'...")
    engine = create_engine(
        f"postgresql://{creds['username']}:{creds['password']}@{creds['host']}:{creds['port']}/{creds['db_name']}"
    )
    
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"Successfully loaded data into the '{table_name}' table!")
    
    engine.dispose()
    print("Database connections cleanly closed.")

if __name__ == "__main__":
    print("This module is meant to be run from main.py")