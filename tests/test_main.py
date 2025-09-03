"""Tests for the main module."""

import pytest
from unittest.mock import patch, MagicMock
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import main


class TestMain:
    """Test cases for main module functions."""
    
    @patch('main.setup_logging')
    @patch('builtins.print')
    def test_main_function(self, mock_print, mock_setup_logging):
        """Test the main function executes without errors."""
        # Run the main function
        main()
        
        # Assert logging was setup
        mock_setup_logging.assert_called_once()
        
        # Assert print statements were called
        assert mock_print.call_count >= 2
        mock_print.assert_any_call("Hello from Claude Test!")
        mock_print.assert_any_call("This is a well-structured Python project.")
    
    @patch.dict(os.environ, {'LOG_LEVEL': 'DEBUG'})
    @patch('main.setup_logging')
    def test_main_with_debug_logging(self, mock_setup_logging):
        """Test main function with DEBUG log level from environment."""
        main()
        mock_setup_logging.assert_called_once_with('DEBUG')