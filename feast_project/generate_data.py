# generate_data.py
# Creates and saves sample data for the Feast demo

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from pathlib import Path

project_dir = Path("feast_demo")
data_dir = project_dir / "data"
data_dir.mkdir(exist_ok=True)

# Generate sample data
current_time = datetime.now()
n_customers = 1000

# Transaction dataset
transaction_data = {
    "event_timestamp": [current_time - timedelta(days=np.random.randint(1, 30)) for _ in range(n_customers * 5)],
    "customer_id": np.random.randint(1, n_customers + 1, size=n_customers * 5),
    "transaction_amount": np.random.uniform(10, 1000, size=n_customers * 5),
    "merchant_category": np.random.choice(["food", "retail", "entertainment", "travel", "other"], size=n_customers * 5),
    "transaction_count": np.random.randint(1, 10, size=n_customers * 5)
}

# Customer dataset
customer_data = {
    "event_timestamp": [current_time - timedelta(days=np.random.randint(1, 30)) for _ in range(n_customers)],
    "customer_id": range(1, n_customers + 1),
    "age": np.random.randint(18, 80, size=n_customers),
    "city": np.random.choice(["New York", "San Francisco", "Chicago", "Los Angeles", "Miami"], size=n_customers),
    "signup_date": [current_time - timedelta(days=np.random.randint(30, 365)) for _ in range(n_customers)]
}

# Convert to DataFrames
transactions_df = pd.DataFrame(transaction_data)
customers_df = pd.DataFrame(customer_data)

# Save data to parquet files
transactions_df.to_parquet(data_dir / "transactions.parquet")
customers_df.to_parquet(data_dir / "customers.parquet")

print(f"Generated and saved transaction data for {n_customers} customers")
print(f"Transaction data shape: {transactions_df.shape}")
print(f"Customer data shape: {customers_df.shape}")