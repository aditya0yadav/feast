# setup.py
# Creates the necessary directory structure and initial files for a Feast project

import os
from pathlib import Path

# Create project directory structure
project_dir = Path("feast_demo")
project_dir.mkdir(exist_ok=True)
data_dir = project_dir / "data"
data_dir.mkdir(exist_ok=True)

# Create feature_store.yaml configuration file
feature_store_yaml = """
project: feast_demo
registry: data/registry.db
provider: local
online_store:
    type: sqlite
    path: data/online_store.db
"""

with open(project_dir / "feature_store.yaml", "w") as f:
    f.write(feature_store_yaml)

print(f"Project structure created at {project_dir}")