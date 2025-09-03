# Claude Test

A test repository created with Claude using standard project structure and best practices.

## Project Structure

```
claude_test/
├── src/                    # Source code
│   ├── __init__.py
│   ├── main.py            # Main application entry point
│   └── utils/             # Utility modules
│       └── __init__.py
├── tests/                 # Test files
│   ├── __init__.py
│   ├── test_main.py
│   └── test_utils/
│       └── __init__.py
├── docs/                  # Documentation
│   └── README.md
├── data/                  # Data files
│   ├── raw/              # Raw, unprocessed data
│   ├── processed/        # Cleaned, processed data
│   └── external/         # Data from external sources
├── notebooks/            # Jupyter notebooks for exploration
├── scripts/              # Standalone scripts
├── config/               # Configuration files
├── requirements.txt      # Python dependencies
├── setup.py             # Package setup
├── .gitignore           # Git ignore rules
├── .env.example         # Environment variables example
└── README.md            # This file
```

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/gseemann/claude_test.git
   cd claude_test
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Copy environment variables:
   ```bash
   cp .env.example .env
   ```

5. Run the application:
   ```bash
   python src/main.py
   ```

## Testing

Run tests using pytest:
```bash
pytest tests/
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.