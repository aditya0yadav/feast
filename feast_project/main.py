# main.py
# Main script to run the entire Feast demo

import os
import importlib.util
from pathlib import Path

def run_feast_demo():
    # Create base project directory if it doesn't exist
    project_base = Path(".")
    
    # Define all script files
    script_files = {
        "setup.py": "Project Setup",
        "generate_data.py": "Data Generation",
        "feast_operations.py": "Feast Operations",
        "feature_retrieval.py": "Feature Retrieval Examples"
    }
    
    # Run each script in order
    for script_file, description in script_files.items():
        full_path = project_base / script_file
        
        if not full_path.exists():
            print(f"Error: {script_file} not found!")
            continue
        
        print(f"\n{'='*50}")
        print(f"Running {description}: {script_file}")
        print(f"{'='*50}\n")
        
        # Import and run the script
        spec = importlib.util.spec_from_file_location("module.name", full_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        if script_file == "feast_operations.py" and hasattr(module, "run_feast_operations"):
            module.run_feast_operations()
        elif script_file == "feature_retrieval.py" and hasattr(module, "demonstrate_feature_retrieval"):
            module.demonstrate_feature_retrieval()
    
    print("\nFeast demo completed successfully!")

if __name__ == "__main__":
    run_feast_demo()