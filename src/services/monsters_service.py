"""
Monsters service for Fibulopedia.

This module handles loading, parsing, and querying monster data.
Supports searching by name, location, and loot.
"""

from typing import Optional

import streamlit as st

from src.config import MONSTERS_FILE
from src.models import Monster
from src.services.data_loader import (
    load_json,
    validate_required_fields,
    safe_int
)
from src.logging_utils import setup_logger

logger = setup_logger(__name__)


def load_monsters() -> list[Monster]:
    """
    Load all monsters from the monsters.json file.
    
    Returns:
        List of Monster objects, or an empty list if loading fails.
    
    Example:
        >>> monsters = load_monsters()
        >>> print(f"Loaded {len(monsters)} monsters")
    """
    data = load_json(MONSTERS_FILE)
    
    if not data or not isinstance(data, list):
        logger.warning("No monsters data available or invalid format")
        return []
    
    monsters = []
    for item in data:
        if not validate_required_fields(
            item,
            ["id", "name", "hp", "exp", "loot", "location"],
            "Monster"
        ):
            continue
        
        try:
            monster = Monster(
                id=str(item["id"]),
                name=str(item["name"]),
                hp=safe_int(item["hp"]),
                exp=safe_int(item["exp"]),
                loot=str(item["loot"]),
                location=str(item["location"]),
                difficulty=item.get("difficulty")
            )
            monsters.append(monster)
        except Exception as e:
            logger.error(f"Error parsing monster {item.get('id', 'unknown')}: {e}")
    
    logger.info(f"Loaded {len(monsters)} monsters")
    return monsters


def get_monster_by_id(monster_id: str) -> Optional[Monster]:
    """
    Get a specific monster by its ID.
    
    Args:
        monster_id: The unique ID of the monster.
    
    Returns:
        The Monster object if found, None otherwise.
    
    Example:
        >>> monster = get_monster_by_id("monster_001")
        >>> if monster:
        ...     print(monster.name)
    """
    monsters = load_monsters()
    for monster in monsters:
        if monster.id == monster_id:
            return monster
    return None


def search_monsters(query: str) -> list[Monster]:
    """
    Search monsters by name, location, or loot.
    
    Args:
        query: The search query string.
    
    Returns:
        List of monsters matching the query.
    
    Example:
        >>> results = search_monsters("dragon")
    """
    if not query:
        return load_monsters()
    
    monsters = load_monsters()
    query_lower = query.lower()
    
    results = [
        monster for monster in monsters
        if (query_lower in monster.name.lower() or
            query_lower in monster.location.lower() or
            query_lower in monster.loot.lower())
    ]
    
    logger.info(f"Search for '{query}' found {len(results)} monsters")
    return results


def filter_monsters_by_location(location: str) -> list[Monster]:
    """
    Filter monsters by location.
    
    Args:
        location: The location to filter by.
    
    Returns:
        List of monsters in the specified location.
    
    Example:
        >>> monsters = filter_monsters_by_location("Thais")
    """
    monsters = load_monsters()
    location_lower = location.lower()
    return [m for m in monsters if location_lower in m.location.lower()]


def get_locations() -> list[str]:
    """
    Get all unique monster locations.
    
    Returns:
        List of location strings.
    
    Example:
        >>> locations = get_locations()
        >>> print(locations)  # ['Thais', 'Carlin', 'Edron', ...]
    """
    monsters = load_monsters()
    locations = sorted(set(monster.location for monster in monsters))
    return locations
