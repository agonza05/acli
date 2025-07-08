"""This module provides config env functionality."""

# acli/config/environment.py

import os
import typer

from acli import GLOBAL_ENVVAR_PREFIX


app = typer.Typer()


@app.command()
def env() -> None:
    """Show envrionment variables."""

    for key, value in os.environ.items():
        if key.startswith(GLOBAL_ENVVAR_PREFIX):
            typer.echo(f"{key}={value}")
