"""This module provides personio status."""

# acli/personio/get.py

import typer
import requests

from acli import ERRORS, CONN_ERROR
from . import PERSONIO_STATUS_URL


app = typer.Typer()


@app.command()
def status() -> None:
    """Check Personio API status."""

    try:
        response = requests.get(PERSONIO_STATUS_URL)
    except OSError:
        typer.secho(
            f"API request failed. Error {ERRORS[CONN_ERROR]}",
            fg=typer.colors.RED,
        )
        raise typer.Exit()
    if response.json()["status"]["indicator"] == "none":
        text_color = typer.colors.GREEN
    else:
        text_color = typer.colors.RED
    typer.secho(f"{response.json()['status']['description']}", fg=text_color)
