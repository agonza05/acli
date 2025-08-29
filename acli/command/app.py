"""This module provides command commands."""

# acli/command/app.py

import typer
from acli.helpers import run_cmd

app = typer.Typer()


@app.command()
def new() -> None:
    """Generate templates to develop a new cli command."""

    run_cmd(["touch", "main.py", "config.py", "utils.py"])
    typer.secho("Templates generated successfully.", fg=typer.colors.GREEN)
