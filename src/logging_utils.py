"""
Logging utilities for Fibulopedia.

This module provides centralized logging configuration for the application.
It sets up a consistent logging format and level across all modules.
"""

import logging
import sys
from typing import Optional

from src.config import LOG_LEVEL, LOG_FORMAT, LOG_DATE_FORMAT


def setup_logger(name: str, level: Optional[str] = None) -> logging.Logger:
    """
    Set up and configure a logger with the specified name.
    
    Args:
        name: The name of the logger (typically __name__ of the module).
        level: The logging level as a string (DEBUG, INFO, WARNING, ERROR, CRITICAL).
               If None, uses the LOG_LEVEL from config.
    
    Returns:
        A configured logger instance.
    
    Example:
        >>> logger = setup_logger(__name__)
        >>> logger.info("Application started")
    """
    logger = logging.getLogger(name)
    
    # Set logging level
    log_level = level if level else LOG_LEVEL
    logger.setLevel(getattr(logging, log_level.upper(), logging.INFO))
    
    # Avoid adding multiple handlers if logger already configured
    if not logger.handlers:
        # Create console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logger.level)
        
        # Create formatter
        formatter = logging.Formatter(
            fmt=LOG_FORMAT,
            datefmt=LOG_DATE_FORMAT
        )
        console_handler.setFormatter(formatter)
        
        # Add handler to logger
        logger.addHandler(console_handler)
    
    return logger


def log_exception(logger: logging.Logger, exception: Exception, context: str = "") -> None:
    """
    Log an exception with optional context.
    
    Args:
        logger: The logger instance to use.
        exception: The exception to log.
        context: Optional context string describing where the exception occurred.
    
    Example:
        >>> try:
        ...     risky_operation()
        ... except Exception as e:
        ...     log_exception(logger, e, "Failed to load data")
    """
    if context:
        logger.error(f"{context}: {type(exception).__name__}: {str(exception)}", exc_info=True)
    else:
        logger.error(f"{type(exception).__name__}: {str(exception)}", exc_info=True)


# Pre-configured logger for general application use
app_logger = setup_logger("fibulopedia")
