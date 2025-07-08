"""This module provides config commands."""

# acli/config/app.py

import typer

from .path import app as path_app
from .environment import app as env_app
from .show import app as show_app

app = typer.Typer()

app.add_typer(path_app)
app.add_typer(env_app)
app.add_typer(show_app)
