"""This module provides system packages functionality."""

# acli/system/packages.py

import typer

from acli.helpers import run_cmd

app = typer.Typer()


@app.command()
def up() -> None:
    """Upgrade brew packages."""

    brew_commands = ["update", "upgrade", "cleanup"]

    for command in brew_commands:
        run_cmd(["brew", command])
    typer.secho("Packages upgraded successfully.", fg=typer.colors.GREEN)
