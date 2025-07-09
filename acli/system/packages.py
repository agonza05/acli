"""This module provides system packages functionality."""

# acli/system/packages.py

import typer
from rich.progress import Progress, SpinnerColumn, TextColumn

from acli.helpers import run_cmd

app = typer.Typer()


@app.command()
def up() -> None:
    """Upgrade brew packages."""

    brew_commands = ["update", "upgrade", "cleanup"]

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        task = progress.add_task(
            description="[magenta]Updating packages...", total=len(brew_commands)
        )
        for command in brew_commands:
            progress.console.print(f" - brew {command}...")
            run_cmd(["brew", command])
            progress.advance(task)

    typer.secho("Packages upgraded successfully.", fg=typer.colors.GREEN)
