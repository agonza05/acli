"""This module provides config show functionality."""

# acli/config/info.py

import typer

from acli.configinit import config_file_path


app = typer.Typer()


@app.command()
def show() -> None:
    """Show app configuration."""

    with open(config_file_path, "r") as file:
        file_content = file.read()
        typer.echo(file_content)
