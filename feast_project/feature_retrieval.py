# feature_retrieval.py
# Demonstrates different ways to retrieve features from Feast

import pandas as pd
from datetime import datetime, timedelta
from feast import FeatureStore
import os
from pathlib import Path

def demonstrate_feature_retrieval():
    # Change to project directory
    os.chdir(Path("feast_demo"))
    
    # Initialize the feature store
    store = FeatureStore(repo_path=".")
    
    print("Feature Retrieval Examples:")
    print("==========================")
    
    # Example 1: Retrieve specific features for specific entities
    print("\nExample 1: Specific features for specific entities")
    features_1 = store.get_online_features(
        features=[
            "transaction_features:transaction_amount",
            "customer_features:age",
        ],
        entity_rows=[{"customer_id": 1}, {"customer_id": 5}, {"customer_id": 10}]
    ).to_dict()
    
    print("Results:")
    for key, value in features_1.items():
        print(f"{key}: {value}")
    
    # Example 2: Retrieve all features from a feature view
    print("\nExample 2: All features from a feature view")
    features_2 = store.get_online_features(
        features=[
            "transaction_features:*",
        ],
        entity_rows=[{"customer_id": 1}]
    ).to_dict()
    
    print("Results:")
    for key, value in features_2.items():
        print(f"{key}: {value}")
    
    # Example 3: Historical feature retrieval with time travel
    print("\nExample 3: Historical feature retrieval with time travel")
    entity_df = pd.DataFrame(
        {
            "customer_id": [1, 2, 3],
            "event_timestamp": [
                datetime.now() - timedelta(days=7),
                datetime.now() - timedelta(days=14),
                datetime.now() - timedelta(days=21)
            ]
        }
    )
    
    historical_features = store.get_historical_features(
        entity_df=entity_df,
        features=[
            "transaction_features:transaction_amount",
            "transaction_features:transaction_count",
            "customer_features:age",
        ],
    ).to_df()
    
    print("Results:")
    print(historical_features)
    
    # Example 4: Using a feature service
    print("\nExample 4: Using a feature service")
    service_features = store.get_online_features(
        features=store.get_feature_service("ml_features"),
        entity_rows=[{"customer_id": 42}]
    ).to_dict()
    
    print("Results:")
    for key, value in service_features.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    demonstrate_feature_retrieval()