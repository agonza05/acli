"""This module provides dockercreds commands."""

# acli/dockercreds/app.py

import typer

from .credentials.app import app as credentials_app

app = typer.Typer()

app.add_typer(credentials_app, name="credentials", help="Docker credentials commands.")
