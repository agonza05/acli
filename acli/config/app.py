"""This module provides config commands."""

# acli/config/app.py

import os
import typer

from acli import GLOBAL_ENVVAR_PREFIX
from acli.configinit import (
    config_dir_path,
    config_file_path,
    CONFIG_FILE_NAME,
    ENV_FILE_NAME,
)

app = typer.Typer()


@app.command()
def show() -> None:
    """Show app configuration."""

    with open(config_file_path, "r") as file:
        file_content = file.read()
        typer.echo(file_content)


@app.command()
def env() -> None:
    """Show envrionment variables."""

    for key, value in os.environ.items():
        if key.startswith(GLOBAL_ENVVAR_PREFIX):
            typer.echo(f"{key}={value}")


@app.command()
def path() -> None:
    """Display full path of configuration files."""

    typer.echo(
        f"Configuration files are located in: {str(config_dir_path)}",
    )
    typer.echo(
        f"App configuration is taken from: {CONFIG_FILE_NAME}",
    )
    typer.echo(
        f"Envrionment variables are sourced from: {ENV_FILE_NAME}",
    )
