"""
Configuration module for Fibulopedia.

This module contains all configuration constants, paths, and theme settings
used throughout the application. Centralizing configuration makes it easy
to modify behavior without changing code in multiple places.
"""

import os
from pathlib import Path
from typing import Final

# Base paths
PROJECT_ROOT: Final[Path] = Path(__file__).parent.parent
CONTENT_DIR: Final[Path] = PROJECT_ROOT / "content"
ASSETS_DIR: Final[Path] = PROJECT_ROOT / "assets"

# Content file paths
WEAPONS_FILE: Final[Path] = CONTENT_DIR / "weapons.json"
EQUIPMENT_FILE: Final[Path] = CONTENT_DIR / "equipment.json"
SPELLS_FILE: Final[Path] = CONTENT_DIR / "spells.json"
MONSTERS_FILE: Final[Path] = CONTENT_DIR / "monsters.json"
QUESTS_FILE: Final[Path] = CONTENT_DIR / "quests.json"
SERVER_INFO_FILE: Final[Path] = CONTENT_DIR / "server_info.json"
LANGUAGES_FILE: Final[Path] = CONTENT_DIR / "languages.json"

# Asset paths
LOGO_PATH: Final[Path] = ASSETS_DIR / "logo_fibulopedia.png"
MAP_PATH: Final[Path] = ASSETS_DIR / "map_7.1.png"
STYLES_PATH: Final[Path] = ASSETS_DIR / "styles.css"

# Application settings
APP_TITLE: Final[str] = "Fibulopedia"
APP_SUBTITLE: Final[str] = "Unofficial guide and wiki for Fibula Project - a Tibia 7.1 style OTS"
APP_ICON: Final[str] = "🗡️"

# Theme configuration
class Theme:
    """Theme configuration for the application."""
    
    # Color scheme
    PRIMARY_COLOR: Final[str] = "#d4af37"  # Gold
    SECONDARY_COLOR: Final[str] = "#8b7355"  # Bronze
    BACKGROUND_COLOR: Final[str] = "#1a1a1a"  # Dark grey
    SURFACE_COLOR: Final[str] = "#2d2d2d"  # Lighter grey
    TEXT_COLOR: Final[str] = "#e0e0e0"  # Light grey
    TEXT_MUTED: Final[str] = "#a0a0a0"  # Muted grey
    
    # Accent colors
    SUCCESS_COLOR: Final[str] = "#4caf50"
    WARNING_COLOR: Final[str] = "#ff9800"
    ERROR_COLOR: Final[str] = "#f44336"
    INFO_COLOR: Final[str] = "#2196f3"
    
    # Font settings
    FONT_FAMILY: Final[str] = "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif"
    HEADING_FONT: Final[str] = "'Palatino Linotype', 'Book Antiqua', Palatino, serif"
    
    # Layout
    MAX_CONTENT_WIDTH: Final[int] = 1200  # pixels
    CARD_BORDER_RADIUS: Final[str] = "8px"
    CARD_PADDING: Final[str] = "1.5rem"


# Language configuration
class Language:
    """Language configuration for future multi-language support."""
    
    SUPPORTED_LANGUAGES: Final[dict[str, str]] = {
        "en": "English",
        "pl": "Polski",
        "sv": "Svenska",
        "pt_br": "Português (Brasil)"
    }
    
    DEFAULT_LANGUAGE: Final[str] = "en"


# Navigation configuration
NAVIGATION_ITEMS: Final[list[dict[str, str]]] = [
    {"name": "Home", "icon": "🏠", "description": "Return to the main hub"},
    {"name": "Weapons", "icon": "⚔️", "description": "Browse all weapons"},
    {"name": "Equipment", "icon": "🛡️", "description": "View equipment by slot"},
    {"name": "Spells", "icon": "✨", "description": "Discover spells and incantations"},
    {"name": "Monsters", "icon": "👹", "description": "Check monster stats and loot"},
    {"name": "Quests", "icon": "📜", "description": "Explore available quests"},
    {"name": "Map", "icon": "🗺️", "description": "View the world map"},
    {"name": "Server Info", "icon": "ℹ️", "description": "Server rates and information"},
    {"name": "Search", "icon": "🔍", "description": "Advanced search across all content"},
    {"name": "About", "icon": "📖", "description": "About Fibulopedia"},
]

# Hub cards configuration for home page
HUB_CARDS: Final[list[dict[str, str]]] = [
    {
        "title": "Weapons",
        "icon": "⚔️",
        "description": "Browse all weapons available on the server. View stats, compare items, and find out where to get them.",
        "page": "Weapons"
    },
    {
        "title": "Equipment",
        "icon": "🛡️",
        "description": "Check armor, helmets, boots, and other equipment pieces. Organize by slot and compare defense values.",
        "page": "Equipment"
    },
    {
        "title": "Spells",
        "icon": "✨",
        "description": "Discover all spells and their incantations. Filter by vocation, level, and mana cost.",
        "page": "Spells"
    },
    {
        "title": "Monsters",
        "icon": "👹",
        "description": "Check monsters, their HP, EXP rewards, and valuable loot. Plan your hunts efficiently.",
        "page": "Monsters"
    },
    {
        "title": "Quests",
        "icon": "📜",
        "description": "Explore available quests, their locations, and rewards. Never miss a quest again.",
        "page": "Quests"
    },
    {
        "title": "Map",
        "icon": "🗺️",
        "description": "View the classic Tibia 7.1 world map. Find cities, dungeons, and hunting grounds.",
        "page": "Map"
    },
    {
        "title": "Server Info",
        "icon": "ℹ️",
        "description": "Learn about server rates, rules, and general information. Check what makes Fibula unique.",
        "page": "Server_Info"
    },
    {
        "title": "Search",
        "icon": "🔍",
        "description": "Use advanced search to find anything across all categories. Quick and powerful.",
        "page": "Search"
    },
]

# Logging configuration
LOG_LEVEL: Final[str] = os.getenv("LOG_LEVEL", "INFO")
LOG_FORMAT: Final[str] = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_DATE_FORMAT: Final[str] = "%Y-%m-%d %H:%M:%S"

# Data validation settings
MAX_NAME_LENGTH: Final[int] = 100
MAX_DESCRIPTION_LENGTH: Final[int] = 1000
MIN_HP_VALUE: Final[int] = 1
MAX_HP_VALUE: Final[int] = 100000
MIN_EXP_VALUE: Final[int] = 0
MAX_EXP_VALUE: Final[int] = 1000000

# Search configuration
MAX_SEARCH_RESULTS: Final[int] = 100
SEARCH_SNIPPET_LENGTH: Final[int] = 150
