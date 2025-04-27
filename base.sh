#!/bin/bash

# Create the main project directory
mkdir -p feast_project
cd feast_project

# Create the main Python files (with placeholder content)
touch setup.py
touch generate_data.py
touch features.py
touch feast_operations.py
touch feature_retrieval.py
touch main.py
touch requirements.txt

# Create the feast_demo directory and its structure
mkdir -p feast_demo/data

# Create the feature_store.yaml file (with placeholder content)
echo "project: feast_demo
registry: data/registry.db
provider: local
online_store:
    type: sqlite
    path: data/online_store.db" > feast_demo/feature_store.yaml

# Copy features.py to feast_demo directory
cp features.py feast_demo/

# Create placeholder files for the data directory
# Note: These will be properly generated when you run the actual code
touch feast_demo/data/transactions.parquet
touch feast_demo/data/customers.parquet
touch feast_demo/data/registry.db
touch feast_demo/data/online_store.db

echo "Feast project structure created successfully!"
# Display the created directory structure
find . -type f | sort