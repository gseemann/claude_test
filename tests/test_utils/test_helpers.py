"""Tests for helper functions."""

import pytest
from unittest.mock import patch, MagicMock
import logging
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'src'))

from utils.helpers import setup_logging, validate_config, format_message


class TestHelpers:
    """Test cases for helper functions."""
    
    def test_format_message_without_prefix(self):
        """Test format_message without prefix."""
        result = format_message("test message")
        assert result == "test message"
    
    def test_format_message_with_prefix(self):
        """Test format_message with prefix."""
        result = format_message("test message", "INFO")
        assert result == "[INFO] test message"
    
    def test_format_message_with_none_prefix(self):
        """Test format_message with None prefix."""
        result = format_message("test message", None)
        assert result == "test message"
    
    def test_validate_config(self):
        """Test validate_config function."""
        result = validate_config()
        assert result is True
    
    @patch('logging.basicConfig')
    def test_setup_logging_default(self, mock_basic_config):
        """Test setup_logging with default level."""
        setup_logging()
        mock_basic_config.assert_called_once()
        args, kwargs = mock_basic_config.call_args
        assert kwargs['level'] == logging.INFO
    
    @patch('logging.basicConfig')
    def test_setup_logging_debug(self, mock_basic_config):
        """Test setup_logging with DEBUG level."""
        setup_logging("DEBUG")
        mock_basic_config.assert_called_once()
        args, kwargs = mock_basic_config.call_args
        assert kwargs['level'] == logging.DEBUG