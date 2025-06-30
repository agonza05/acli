"""This module provides personio employee."""

# acli/personio/employee.py

import typer
import requests

from . import CLIENT_ID_OPTIONS, CLIENT_SECRET_OPTIONS, EMPLOYEE_ID_OPTIONS
from .auth import _auth_request


app = typer.Typer()


@app.command()
def employee(
    client_id: CLIENT_ID_OPTIONS,
    client_secret: CLIENT_SECRET_OPTIONS,
    employee_id: EMPLOYEE_ID_OPTIONS,
) -> None:
    """Get my infomration from Personio."""

    endpoint_url = "https://api.personio.de/v1/company/employees/" + employee_id
    response = _auth_request(client_id, client_secret)
    access_token = response.json()["access_token"]
    headers = {"accept": "application/json", "authorization": "Bearer " + access_token}
    response = requests.get(endpoint_url, headers=headers)
    response_data = response.json()["data"]["attributes"]

    typer.echo(f"Name: {response_data["preferred_name"]["value"]}")
    typer.echo(f"Email: {response_data["email"]["value"]}")
    typer.echo(f"Department: {response_data["team"]["value"]["attributes"]["name"]}")
    typer.echo(f"Company: {response_data["subcompany"]["value"]["attributes"]["name"]}")
    typer.echo(f"Status: {response_data["status"]["value"]}")
