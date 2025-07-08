"""This module provides personio employee."""

# acli/personio/employee.py

import typer
import requests

from acli.helpers import validate_http_status_code
from . import CLIENT_ID_OPTIONS, CLIENT_SECRET_OPTIONS, EMPLOYEE_ID_OPTIONS
from .auth import get_auth_token


app = typer.Typer()


@app.command()
def employee(
    client_id: CLIENT_ID_OPTIONS,
    client_secret: CLIENT_SECRET_OPTIONS,
    employee_id: EMPLOYEE_ID_OPTIONS,
) -> None:
    """Get my infomration from Personio."""

    endpoint_url = "https://api.personio.de/v1/company/employees/" + employee_id
    access_token = get_auth_token(client_id, client_secret)
    headers = {"accept": "application/json", "authorization": f"Bearer {access_token}"}
    response = requests.get(endpoint_url, headers=headers)
    validate_http_status_code(response)
    json_data = response.json()["data"]["attributes"]

    typer.echo(f"Name: {json_data["preferred_name"]["value"]}")
    typer.echo(f"Email: {json_data["email"]["value"]}")
    typer.echo(f"Department: {json_data["team"]["value"]["attributes"]["name"]}")
    typer.echo(f"Company: {json_data["subcompany"]["value"]["attributes"]["name"]}")
    typer.echo(f"Status: {json_data["status"]["value"]}")
