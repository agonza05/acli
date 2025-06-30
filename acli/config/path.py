"""This module provides config path functionality."""

# acli/config/path.py

import typer

from . import (
    config_file_path,
    env_file_path,
    config_dir_path,
    CONFIG_FILE_NAME,
    ENV_FILE_NAME,
)


app = typer.Typer()


@app.command()
def path() -> None:
    """Display full path of configuration files."""
    if not (env_file_path.exists() and config_file_path.exists()):
        typer.secho(
            "Configuration files do not exist. Please run `config init` first.",
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    else:
        typer.echo(
            f"Configuration files are located in: {str(config_dir_path)}",
        )
        typer.echo(
            f"App configuration is taken from: {CONFIG_FILE_NAME}",
        )
        typer.echo(
            f"Envrionment variables are sourced from: {ENV_FILE_NAME}",
        )
