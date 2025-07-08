"""This module provides personio auth."""

# acli/personio/auth.py

import typer
import requests

from acli import NET_CONN_ERROR, JSON_DATA_ERROR
from acli.helpers import error_and_exit, validate_http_status_code
from . import CLIENT_ID_OPTIONS, CLIENT_SECRET_OPTIONS, PERSONIO_BASE_URL


app = typer.Typer()


def get_auth_token(client_id: str, client_secret: str) -> str | None:
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
        validate_http_status_code(response)
        json_data = response.json()
        if "access_token" in json_data:
            return json_data["access_token"]
        else:
            error_and_exit(JSON_DATA_ERROR, "No auth token found in response.")
    except requests.exceptions.RequestException as e:
        error_and_exit(NET_CONN_ERROR, f"API request error. {e.strerror}")


@app.command()
def auth(
    client_id: CLIENT_ID_OPTIONS,
    client_secret: CLIENT_SECRET_OPTIONS,
) -> None:
    """Authenticates with Personio API."""

    auth_token = get_auth_token(client_id, client_secret)
    typer.echo(auth_token)
