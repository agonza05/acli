"""This module provides personio auth."""

# acli/personio/auth.py

import typer
import requests

from acli import NET_CONN_ERROR
from acli.helpers import error_and_exit, validate_http_status_code, validate_json_key
from . import CLIENT_ID_OPTIONS, CLIENT_SECRET_OPTIONS, PERSONIO_BASE_URL


app = typer.Typer()


def get_auth_token(client_id: str, client_secret: str) -> str:
    """Helper function to get auth token from Personio API."""

    return_data = ""
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
        validate_json_key("access_token", json_data)
        return_data = json_data["access_token"]
    except requests.exceptions.RequestException as e:
        error_and_exit(NET_CONN_ERROR, f"API request error. {e.strerror}")
    return return_data


@app.command()
def auth(
    client_id: CLIENT_ID_OPTIONS,
    client_secret: CLIENT_SECRET_OPTIONS,
) -> None:
    """Authenticates with Personio API."""

    auth_token = get_auth_token(client_id, client_secret)
    typer.echo(auth_token)
