"""This module provides system commands."""

# acli/system/app.py

import typer

from .info import app as info_app
from .packages import app as packages_app

app = typer.Typer()

app.add_typer(info_app)
app.add_typer(packages_app)
