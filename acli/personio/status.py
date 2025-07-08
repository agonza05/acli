"""This module provides personio status."""

# acli/personio/status.py

import typer
import requests

from acli import NET_CONN_ERROR
from acli.helpers import error_and_exit
from . import PERSONIO_STATUS_URL


app = typer.Typer()


@app.command()
def status() -> None:
    """Check Personio API status."""

    try:
        response = requests.get(PERSONIO_STATUS_URL)
        if response.json()["status"]["indicator"] == "none":
            text_color = typer.colors.GREEN
        else:
            text_color = typer.colors.RED
        typer.secho(f"{response.json()['status']['description']}", fg=text_color)
    except OSError:
        error_and_exit(NET_CONN_ERROR, "API request failed.")
