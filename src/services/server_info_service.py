"""
Server info service for Fibulopedia.

This module handles loading and providing server information
such as rates, version, and general details.
"""

from typing import Optional

import streamlit as st

from src.config import SERVER_INFO_FILE
from src.models import ServerInfo
from src.services.data_loader import load_json
from src.logging_utils import setup_logger

logger = setup_logger(__name__)


def load_server_info() -> Optional[ServerInfo]:
    """
    Load server information from the server_info.json file.
    
    Returns:
        ServerInfo object if successful, None otherwise.
    
    Example:
        >>> info = load_server_info()
        >>> if info:
        ...     print(f"Server: {info.name}")
    """
    data = load_json(SERVER_INFO_FILE)
    
    if not data or not isinstance(data, dict):
        logger.warning("No server info data available or invalid format")
        return None
    
    try:
        server_info = ServerInfo(
            id=str(data.get("id", "server_001")),
            name=str(data.get("name", "Fibula Project")),
            description=str(data.get("description", "")),
            rates=data.get("rates", {}),
            version=str(data.get("version", "7.1")),
            website=data.get("website"),
            discord=data.get("discord"),
            additional_info=data.get("additional_info")
        )
        logger.info("Successfully loaded server info")
        return server_info
    except Exception as e:
        logger.error(f"Error parsing server info: {e}")
        return None


def get_rate(rate_name: str) -> Optional[float | int]:
    """
    Get a specific server rate by name.
    
    Args:
        rate_name: The name of the rate (exp, loot, skill, magic).
    
    Returns:
        The rate value if found, None otherwise.
    
    Example:
        >>> exp_rate = get_rate("exp")
        >>> print(f"EXP Rate: {exp_rate}x")
    """
    server_info = load_server_info()
    if server_info and server_info.rates:
        return server_info.rates.get(rate_name)
    return None
