"""This module provides dockercreds commands."""

# acli/dockercreds/app.py

import typer

from .get import app as get_app

app = typer.Typer()

app.add_typer(get_app)
