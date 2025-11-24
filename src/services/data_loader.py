"""
Data loader service for Fibulopedia.

This module provides generic utilities for loading data from various file
formats (JSON, YAML, CSV) in the content directory. It handles error cases
gracefully and provides consistent error reporting.
"""

import json
from pathlib import Path
from typing import Any, Optional

import streamlit as st

from src.logging_utils import setup_logger

logger = setup_logger(__name__)


def load_json(file_path: Path) -> Optional[list[dict[str, Any]] | dict[str, Any]]:
    """
    Load data from a JSON file.
    
    Args:
        file_path: Path to the JSON file.
    
    Returns:
        The parsed JSON data (typically a list of dicts or a single dict),
        or None if loading fails.
    
    Raises:
        No exceptions are raised; errors are logged and None is returned.
    
    Example:
        >>> data = load_json(Path("content/weapons.json"))
        >>> if data:
        ...     print(f"Loaded {len(data)} weapons")
    """
    if not file_path.exists():
        logger.warning(f"File not found: {file_path}")
        return None
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        logger.info(f"Successfully loaded data from {file_path}")
        return data
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in {file_path}: {e}")
        return None
    except Exception as e:
        logger.error(f"Error loading {file_path}: {e}")
        return None


def save_json(file_path: Path, data: Any, indent: int = 2) -> bool:
    """
    Save data to a JSON file.
    
    Args:
        file_path: Path to save the JSON file.
        data: The data to serialize to JSON.
        indent: Indentation level for pretty printing.
    
    Returns:
        True if successful, False otherwise.
    
    Example:
        >>> success = save_json(Path("content/weapons.json"), weapons_data)
    """
    try:
        # Ensure parent directory exists
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=indent, ensure_ascii=False)
        
        logger.info(f"Successfully saved data to {file_path}")
        return True
    except Exception as e:
        logger.error(f"Error saving to {file_path}: {e}")
        return False


def validate_required_fields(
    data: dict[str, Any],
    required_fields: list[str],
    entity_name: str = "entity"
) -> bool:
    """
    Validate that all required fields are present in a data dictionary.
    
    Args:
        data: The dictionary to validate.
        required_fields: List of required field names.
        entity_name: Name of the entity type for error messages.
    
    Returns:
        True if all required fields are present, False otherwise.
    
    Example:
        >>> is_valid = validate_required_fields(
        ...     weapon_data,
        ...     ["id", "name", "attack", "defense"],
        ...     "Weapon"
        ... )
    """
    missing_fields = [field for field in required_fields if field not in data]
    
    if missing_fields:
        logger.warning(
            f"{entity_name} missing required fields: {', '.join(missing_fields)}"
        )
        return False
    
    return True


def safe_int(value: Any, default: int = 0) -> int:
    """
    Safely convert a value to an integer.
    
    Args:
        value: The value to convert.
        default: Default value if conversion fails.
    
    Returns:
        The integer value or the default.
    
    Example:
        >>> hp = safe_int(monster_data.get("hp"), default=100)
    """
    try:
        return int(value)
    except (ValueError, TypeError):
        return default


def safe_float(value: Any, default: float = 0.0) -> float:
    """
    Safely convert a value to a float.
    
    Args:
        value: The value to convert.
        default: Default value if conversion fails.
    
    Returns:
        The float value or the default.
    
    Example:
        >>> weight = safe_float(item_data.get("weight"), default=1.0)
    """
    try:
        return float(value)
    except (ValueError, TypeError):
        return default


def safe_list(value: Any, default: Optional[list] = None) -> list:
    """
    Safely convert a value to a list.
    
    Args:
        value: The value to convert.
        default: Default value if conversion fails.
    
    Returns:
        The list value or the default (empty list if default is None).
    
    Example:
        >>> dropped_by = safe_list(item_data.get("dropped_by"))
    """
    if default is None:
        default = []
    
    if isinstance(value, list):
        return value
    elif value is None:
        return default
    else:
        return [value]
