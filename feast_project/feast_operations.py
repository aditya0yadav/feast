# feast_operations.py - corrected version

import pandas as pd
from datetime import datetime, timedelta
from feast import FeatureStore
import os
from pathlib import Path

# Import the feature objects from features.py
from features import customer, transaction_features, customer_features, ml_feature_service

def run_feast_operations():
    # Change to project directory
    os.chdir(Path("feast_demo"))
    
    # Initialize the feature store
    store = FeatureStore(repo_path=".")
    
    # Register the feature views, entities, and other objects
    print("Applying feature definitions...")
    store.apply([customer, transaction_features, customer_features, ml_feature_service])
    
    # Rest of the code remains the same...
    # Materialize the latest features to the online store
    print("Materializing features to online store...")
    store.materialize(
        start_date=datetime.now() - timedelta(days=30),
        end_date=datetime.now(),
    )
    
    # Get historical features - create an entity dataframe
    print("Retrieving historical features...")
    entity_df = pd.DataFrame(
        {
            "customer_id": [1, 2, 3, 4, 5],
            "event_timestamp": [datetime.now()] * 5
        }
    )
    
    # Retrieve historical features using the feature service
    training_df = store.get_historical_features(
        entity_df=entity_df,
        features=store.get_feature_service("ml_features"),
    ).to_df()
    
    print("Historical features for training:")
    print(training_df.head())
    
    # Get online features for real-time serving
    print("\nRetrieving online features...")
    online_features = store.get_online_features(
        features=[
            "transaction_features:transaction_amount",
            "transaction_features:merchant_category",
            "transaction_features:transaction_count",
            "customer_features:age",
            "customer_features:city",
        ],
        entity_rows=[{"customer_id": 1}, {"customer_id": 2}]
    ).to_dict()
    
    print("Online features for real-time serving:")
    for key, value in online_features.items():
        print(f"{key}: {value}")
    
    return store, training_df, online_features

if __name__ == "__main__":
    run_feast_operations()