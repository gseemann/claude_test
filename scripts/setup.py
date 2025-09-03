#!/usr/bin/env python3
"""Setup script for development environment.

This script helps set up the development environment for the claude_test project.
"""

import os
import subprocess
import sys
from pathlib import Path


def run_command(command: str) -> bool:
    """Run a shell command and return success status.
    
    Args:
        command: The command to run
        
    Returns:
        True if command succeeded, False otherwise
    """
    try:
        subprocess.run(command, shell=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error running command '{command}': {e}")
        return False


def setup_environment():
    """Set up the development environment."""
    print("Setting up claude_test development environment...")
    
    # Check if we're in a virtual environment
    if sys.prefix == sys.base_prefix:
        print("Warning: Not running in a virtual environment!")
        print("Consider creating one with: python -m venv venv")
        print("And activating it with: source venv/bin/activate (or venv\\Scripts\\activate on Windows)")
    
    # Install dependencies
    print("Installing dependencies...")
    if not run_command("pip install -r requirements.txt"):
        print("Failed to install dependencies")
        return False
    
    # Create .env file if it doesn't exist
    if not Path(".env").exists():
        print("Creating .env file from template...")
        if Path(".env.example").exists():
            run_command("cp .env.example .env")
        else:
            print("Warning: .env.example not found")
    
    # Install pre-commit hooks (if available)
    if Path(".pre-commit-config.yaml").exists():
        print("Installing pre-commit hooks...")
        run_command("pip install pre-commit")
        run_command("pre-commit install")
    
    print("Setup complete!")
    print("\nNext steps:")
    print("1. Edit .env file with your configuration")
    print("2. Run tests: pytest tests/")
    print("3. Start coding!")
    
    return True


if __name__ == "__main__":
    setup_environment()