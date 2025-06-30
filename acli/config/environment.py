"""This module provides config env and show functionality."""

# acli/config/info.py

import os
import typer
from dotenv import load_dotenv

from . import env_file_path
from acli import GLOBAL_ENVVAR_PREFIX


app = typer.Typer()


def _load_env_vars() -> None:
    """Helper to load envrionment variables."""

    load_dotenv(dotenv_path=env_file_path)


@app.command()
def env() -> None:
    """Show envrionment variables."""

    _load_env_vars()

    for key, value in os.environ.items():
        if key.startswith(GLOBAL_ENVVAR_PREFIX):
            typer.echo(f"{key}={value}")
