# Install instructions

## Requirements

- python 3.13

## Instructions

### Development

1. uv venv .venv --seed --python 3.13
2. uv pip install -e .
3. uv sync
4. uv run start.py

### Permanent

1. uv tool install --reinstall ~/path/to/acli
2. acli
