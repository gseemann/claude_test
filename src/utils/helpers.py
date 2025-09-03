"""Helper functions for the claude_test application.

This module contains various utility functions used throughout the application.
"""

import logging
import sys
from typing import Optional


def setup_logging(level: str = "INFO") -> None:
    """Setup logging configuration.
    
    Args:
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    """
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )


def validate_config() -> bool:
    """Validate application configuration.
    
    Returns:
        True if configuration is valid, False otherwise
    """
    # Add configuration validation logic here
    return True


def format_message(message: str, prefix: Optional[str] = None) -> str:
    """Format a message with optional prefix.
    
    Args:
        message: The message to format
        prefix: Optional prefix to add
        
    Returns:
        Formatted message string
    """
    if prefix:
        return f"[{prefix}] {message}"
    return message