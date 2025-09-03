#!/usr/bin/env python3
"""Main application entry point.

This module serves as the main entry point for the claude_test application.
"""

import logging
import os
from typing import Optional

from utils.helpers import setup_logging


def main() -> None:
    """Main application function."""
    # Setup logging
    log_level = os.getenv("LOG_LEVEL", "INFO")
    setup_logging(log_level)
    
    logger = logging.getLogger(__name__)
    logger.info("Starting Claude Test application")
    
    # Application logic goes here
    print("Hello from Claude Test!")
    print("This is a well-structured Python project.")
    
    logger.info("Application completed successfully")


if __name__ == "__main__":
    main()