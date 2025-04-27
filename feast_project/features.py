# features.py
# Defines entities, feature views, and feature services for Feast

from datetime import timedelta
from feast import Entity, FeatureView, Field, FeatureService
from feast.types import Float32, Int64, String
from feast.infra.offline_stores.file_source import FileSource

# Define Entity
customer = Entity(
    name="customer",
    join_keys=["customer_id"],
    description="Customer identifier"
)

# Define transaction data source
transaction_source = FileSource(
    path="data/transactions.parquet",
    timestamp_field="event_timestamp",
)

# Define customer data source
customer_source = FileSource(
    path="data/customers.parquet",
    timestamp_field="event_timestamp",
)

# Define transaction features
transaction_features = FeatureView(
    name="transaction_features",
    entities=[customer],
    ttl=timedelta(days=90),
    schema=[
        Field(name="transaction_amount", dtype=Float32),
        Field(name="merchant_category", dtype=String),
        Field(name="transaction_count", dtype=Int64),
    ],
    source=transaction_source,
    online=True,
    tags={"team": "transactions"},
)

# Define customer features
customer_features = FeatureView(
    name="customer_features",
    entities=[customer],
    ttl=timedelta(days=365),
    schema=[
        Field(name="age", dtype=Int64),
        Field(name="city", dtype=String),
    ],
    source=customer_source,
    online=True,
    tags={"team": "customers"},
)

# Define a FeatureService to combine features
ml_feature_service = FeatureService(
    name="ml_features",
    features=[
        transaction_features,
        customer_features
    ],
)