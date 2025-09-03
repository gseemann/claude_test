# Documentation

This directory contains project documentation.

## Structure

- `README.md` - This file, overview of documentation
- `api.md` - API documentation (to be added)
- `setup.md` - Setup and installation guide (to be added)
- `contributing.md` - Contribution guidelines (to be added)

## Building Documentation

To build the documentation using Sphinx:

```bash
# Install documentation dependencies
pip install sphinx sphinx-rtd-theme

# Initialize Sphinx (run once)
sphinx-quickstart docs/

# Build HTML documentation
sphinx-build -b html docs/ docs/_build/html
```

## Writing Documentation

Documentation should be written in Markdown or reStructuredText format. Follow these guidelines:

1. Use clear, concise language
2. Include code examples where appropriate
3. Keep documentation up to date with code changes
4. Use consistent formatting and style

## API Documentation

API documentation is automatically generated from docstrings in the code. Make sure to:

1. Write comprehensive docstrings for all public functions and classes
2. Follow Google or NumPy docstring conventions
3. Include parameter types and return value documentation
4. Provide usage examples in docstrings