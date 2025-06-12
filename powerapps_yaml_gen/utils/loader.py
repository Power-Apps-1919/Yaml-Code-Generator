import os
import yaml
from typing import Any

def load_yaml_file(path_or_env: str) -> Any:
    """
    Load a YAML file from a file path or an environment variable that stores the path.
    """
    # If it's an environment variable, resolve it
    file_path = os.getenv(path_or_env, path_or_env)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"YAML file not found: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f) or {}
