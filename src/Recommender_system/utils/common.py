import os
import yaml  # Library for parsing YAML files (common for config files)
from src.Recommender_system.logging import logger
import json
import joblib
from ensure import ensure_annotations # Decorator that enforces function parameter types at runtime
from box import ConfigBox # Special dictionary that allows dot notation access (e.g., config.key instead of config['key'])
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError

#This decorator ensures that function arguments match the specified type hints
#If you pass wrong type (e.g., integer instead of Path), it raises an error
#Helps catch type-related bugs early
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file: 
            content= yaml.safe_load(yaml_file) 
                                               
            logger.info(f"yaml file:{path_to_yaml} loaded successfully") 
            return ConfigBox(content)  # Converts dictionary to ConfigBox for dot notation access
                                       # Example: config.database.host instead of config['database']['host']
    
    except BoxValueError:  
        raise ValueError("yaml file is empty")
    except Exception as e: 
        raise e


@ensure_annotations
def create_directories(path_to_directories:list, verbose=True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True) # Creates the directory and any necessary parent directories
        if verbose:
            logger.info(f"created directory at {path}")        
            # Logs the creation (only if verbose is True)




@ensure_annotations
def save_json(path:Path, data: dict):
    with open(path, 'w') as f:     # Opens file in write mode ('w'). Creates file if it doesn't exist, overwrites if it does. 
        json.dump(data,f, indent=4) 
    logger.info(f"json file saved at: {path}")  # Logs confirmation of successful save




@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    with open(path) as f: # Opens the JSON file in read mode
        content= json.load(f) # Parses JSON content into Python dictionary
 
    logger.info(f"json file loaded successfully from:{path}")
    return ConfigBox(content)  # Converts dictionary to ConfigBox for dot notation access



@ensure_annotations
def save_bin(data: Any, path: Path):
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path:Path) -> Any:
    data= joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data



"""
Overall Benefits of the Utility Module
1. Code Reusability & DRY Principle
Common operations are encapsulated once and reused everywhere

Eliminates repetitive code for file operations across the project

Example: Instead of writing file handling code in every module, just call read_yaml()

2. Standardization & Consistency
All file operations follow the same pattern and error handling

Consistent logging format across the entire project

Uniform return types (ConfigBox for configuration files)

3. Type Safety with @ensure_annotations
python
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
Catches type errors early in development

Prevents runtime errors from incorrect parameter types

Self-documenting code through type hints

Benefits by Function
read_yaml()
Security: Uses safe_load() prevents YAML injection attacks

User-friendly access: ConfigBox enables dot notation (config.database.host)

Comprehensive error handling: Specifically catches empty YAML files

Cross-platform: Uses Path objects for platform-independent paths

create_directories()
Batch operations: Creates multiple directories in one call

Idempotent: exist_ok=True means safe to run multiple times

Flexible logging: Optional verbose mode for controlling output

Parent directory creation: Automatically creates nested directories

save_json()
Human-readable: Indented formatting (indent=4) makes files editable

Structured data: Perfect for saving metrics, parameters, and results

Audit trail: Automatic logging of saved files

Overwrite protection: Clear logging helps track file changes

load_json()
Convenient access: ConfigBox conversion for easy data access

Validation: Implicitly validates JSON format during loading

Traceability: Logs which files are loaded and from where

save_bin()
ML-optimized: Joblib is specifically designed for large numpy arrays

Compression: Better storage efficiency for model files

Version tracking: Easy to save multiple model versions

Complete object saving: Preserves entire Python objects, not just data

load_bin()
Production-ready: Fast loading of trained models

Type preservation: Maintains original object types and methods

Consistent interface: Same pattern as other load functions

Project-Level Benefits
1. Simplified Main Pipeline Code
python
# Without utils (messy and repetitive)
def train_pipeline():
    import yaml, json, joblib, os
    with open('config.yaml') as f:
        config = yaml.safe_load(f)
    os.makedirs('models', exist_ok=True)
    with open('metrics.json', 'w') as f:
        json.dump(metrics, f, indent=4)
    joblib.dump(model, 'model.pkl')

# With utils (clean and readable)
def train_pipeline():
    config = read_yaml(Path('config.yaml'))
    create_directories(['models'])
    save_json(Path('metrics.json'), metrics)
    save_bin(model, Path('model.pkl'))
2. Better Debugging & Monitoring
Every operation is logged with timestamps

Track exactly when files were created/modified

Identify which part of pipeline is failing

Monitor file operations in production

3. Error Handling Standardization
Consistent exception handling across all file operations

Meaningful error messages for common issues

Prevents silent failures

4. Development Speed
New team members quickly understand file operations

Less boilerplate code to write

Faster prototyping and experimentation

5. Production Readiness
Joblib's efficiency for model deployment

JSON for human-readable configuration

Proper file handling prevents resource leaks

Logging for monitoring in production

6. Maintainability
Changes to file operations only need to be made in one place

Easy to add new features (e.g., compression, encryption)

Clear separation of concerns

Real-World Impact Example
python
# Without utils - potential issues everywhere
# - Inconsistent error handling
# - Some files not logged
# - Mixed dictionary access patterns
# - Repetitive code in 20+ files

# With utils - clean and maintainable
# - One place to fix all file operations
# - Every operation tracked
# - Consistent dot notation everywhere
# - Type checking prevents bugs
# - Easy to add cloud storage support later
"""