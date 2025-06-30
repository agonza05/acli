"""This module provides personio auth."""

# acli/personio/auth.py

import typer
import requests

from acli import ERRORS, CONN_ERROR
from . import CLIENT_ID_OPTIONS, CLIENT_SECRET_OPTIONS, PERSONIO_BASE_URL


app = typer.Typer()


def _auth_request(client_id: str, client_secret: str) -> requests.models.Response:
    endpoint_url = PERSONIO_BASE_URL + "/auth/token"
    payload = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/x-www-form-urlencoded",
    }
    try:
        response = requests.post(endpoint_url, data=payload, headers=headers)
    except OSError:
        typer.secho(
            f"API authentication failed. Error {ERRORS[CONN_ERROR]}",
            fg=typer.colors.RED,
        )
        raise typer.Exit()
    return response

def _get_auth_token(client_id: str, client_secret: str) -> str:
    response = _auth_request(client_id, client_secret)
    return response.json()["access_token"]

@app.command()
def auth(
    client_id: CLIENT_ID_OPTIONS,
    client_secret: CLIENT_SECRET_OPTIONS,
) -> None:
    """Authenticates with Personio API."""

    auth_token = _get_auth_token(client_id, client_secret)
    typer.echo(auth_token)
