"""This module provides system packages functionality."""

# acli/system/info.py

import typer
import subprocess

from acli import ERRORS, OS_COMMAND_ERROR

app = typer.Typer()


@app.command()
def up() -> None:
    """Upgrade brew packages."""

    commands = [
        "brew update",
        "brew upgrade",
        "brew cleanup"
    ]

    for command in commands:
        result = subprocess.run(command, shell=True)
        if result.returncode != 0:
            typer.secho(
                f"Attendance posting failed. Error {ERRORS[OS_COMMAND_ERROR]}",
                fg=typer.colors.RED,
            )
            raise typer.Exit()
    typer.secho("Packages upgraded successfully.", fg=typer.colors.GREEN)
