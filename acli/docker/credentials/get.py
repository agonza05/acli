"""This module provides docker credentials get functionality."""

# acli/docker/credentials/get.py

import typer

from .vault import get_vault


app = typer.Typer()

# @app.command()
# def get() -> None:
#     registry = sys.stdin.read().strip()
#     get_vault()
#     typer.echo(registry)
