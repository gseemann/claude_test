"""Configuration settings for the claude_test application.

This module contains configuration settings that can be loaded from
environment variables or configuration files.
"""

import os
from pathlib import Path
from typing import Optional


class Settings:
    """Application settings class."""
    
    def __init__(self):
        """Initialize settings from environment variables."""
        # Application settings
        self.app_name: str = os.getenv("APP_NAME", "claude_test")
        self.environment: str = os.getenv("ENVIRONMENT", "development")
        self.debug: bool = os.getenv("DEBUG", "false").lower() == "true"
        
        # Logging settings
        self.log_level: str = os.getenv("LOG_LEVEL", "INFO")
        
        # Database settings (if needed)
        self.database_url: Optional[str] = os.getenv("DATABASE_URL")
        
        # API settings (if needed)
        self.api_key: Optional[str] = os.getenv("API_KEY")
        self.secret_key: Optional[str] = os.getenv("SECRET_KEY")
        
        # Paths
        self.project_root: Path = Path(__file__).parent.parent
        self.data_dir: Path = self.project_root / "data"
        self.logs_dir: Path = self.project_root / "logs"
    
    @property
    def is_development(self) -> bool:
        """Check if running in development environment."""
        return self.environment == "development"
    
    @property
    def is_production(self) -> bool:
        """Check if running in production environment."""
        return self.environment == "production"
    
    def validate(self) -> bool:
        """Validate configuration settings.
        
        Returns:
            True if configuration is valid, False otherwise
        """
        # Add validation logic here
        if self.is_production and self.debug:
            print("Warning: Debug mode enabled in production")
            return False
        
        return True


# Global settings instance
settings = Settings()