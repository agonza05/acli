"""This module provides personio status."""

# acli/personio/status.py

import typer
import requests

from acli import NET_CONN_ERROR
from acli.helpers import error_and_exit, validate_json_key
from . import PERSONIO_STATUS_URL


app = typer.Typer()


@app.command()
def status() -> None:
    """Check Personio API status."""

    try:
        response = requests.get(PERSONIO_STATUS_URL)
        json_data = response.json()
        validate_json_key("status", json_data)
        if json_data["status"]["indicator"] == "none":
            text_color = typer.colors.GREEN
        else:
            text_color = typer.colors.RED
        typer.secho(f"{response.json()['status']['description']}", fg=text_color)
    except OSError:
        error_and_exit(NET_CONN_ERROR, "API request failed.")
