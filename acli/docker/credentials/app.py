"""This module provides docker credentials commands."""

# acli/docker/credentials/app.py

import typer

from .vault import app as vault_app
from .get import app as get_app

app = typer.Typer()

app.add_typer(vault_app)
app.add_typer(get_app)
