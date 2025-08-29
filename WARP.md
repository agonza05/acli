# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

`acli` is a personal CLI tool built with Python and Typer that provides various utility commands. It's a modular CLI application with plugins for system management, Personio HR integration, Docker credential management, and configuration handling.

## Development Commands

### Environment Setup
```bash
# Install in development mode with dependencies
pip install -e ".[dev]"

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On macOS/Linux
```

### Testing
```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=acli

# Run specific test file
pytest tests/test_cli.py
pytest tests/test_system.py
```

### Code Quality
```bash
# Format code
black acli/ tests/

# Sort imports
isort acli/ tests/

# Lint code
flake8 acli/ tests/
```

### Documentation Generation
```bash
# Regenerate README.md from CLI help
bash scripts/generate_docs.sh
```

### Running the CLI
```bash
# Direct Python execution
python start.py [command]

# Using the bin script
bash bin/acli [command]

# After pip install
acli [command]
```

## Architecture Overview

### Core Structure
- **Entry Point**: `acli/main.py` → `acli/cli.py` - Main Typer app with plugin registration
- **Plugin Architecture**: Each major feature is a separate module with its own Typer app
- **Global State**: Managed through module-level dictionaries and environment variables
- **Configuration**: Auto-initialized config files in user app directory using `typer.get_app_dir()`

### Plugin Modules
1. **Config** (`acli/config/`): Configuration management, environment variables, and app settings
2. **System** (`acli/system/`): System information and package management (brew integration)
3. **Personio** (`acli/personio/`): HR system integration with OAuth2 authentication
4. **Docker** (`acli/docker/`): Docker credential management with 1Password integration

### Key Patterns
- **Error Handling**: Centralized error codes and messages in `acli/__init__.py`
- **Environment Variables**: Global prefix `ACLI_` with module-specific sub-prefixes
- **Command Registration**: Each plugin exports a Typer app that gets added to the main app
- **State Management**: Per-plugin state dictionaries (e.g., `PERSONIO_APP_STATE`)
- **Helper Functions**: Common utilities in `acli/helpers.py` for subprocess execution, HTTP validation, table printing

### Configuration System
- Config directory: `~/.local/share/acli/` (or platform equivalent via `typer.get_app_dir()`)
- Files: `config.ini` (unused currently) and `.env` for environment variables
- Auto-initialization on first run with proper file permissions

### Authentication Flow
Personio commands use a callback pattern where credentials are collected once and stored in module state for all subsequent commands in the session.

## Environment Variables

All environment variables use the `ACLI_` prefix:
- `ACLI_PERSONIO_CLIENT_ID`, `ACLI_PERSONIO_CLIENT_SECRET`, `ACLI_PERSONIO_EMPLOYEE_ID`
- `ACLI_PERSONIO_ATTENDANCE_DATE`, `ACLI_PERSONIO_ATTENDANCE_WEEKS`
- `ACLI_DOCKER_VAULT_NAME`

## Testing Strategy

- Uses `typer.testing.CliRunner` for CLI command testing
- Tests focus on exit codes and output validation
- System-level tests validate actual functionality (e.g., brew commands)
- Coverage configured to exclude test files and focus on source code

## Dependencies

### Core Runtime
- `typer`: CLI framework
- `requests`: HTTP client for API integrations
- `psutil`: System information gathering
- `rich`: Enhanced terminal output with tables and progress bars
- `dotenv`: Environment variable management

### Development
- `pytest`: Testing framework with coverage support
- `black`: Code formatting
- `isort`: Import sorting
- `flake8`: Linting
