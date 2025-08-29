"""This module provides personio commands."""

# acli/personio/app.py

import typer
import requests
from typing_extensions import Annotated
from datetime import datetime

from acli.helpers import (
    error_and_exit,
    validate_json_key,
    validate_http_status_code,
    print_table_with_details,
)
from . import COMMAND_ENVVAR_PREFIX, PERSONIO_APP_STATE, PERSONIO_STATUS_URL
from .helpers import (
    get_auth_token,
    create_personio_attendance,
    get_working_days_for_next_four_weeks,
)

app = typer.Typer()


# Get mandatory arguments
@app.callback()
def personio_callback(
    client_id: Annotated[
        str,
        typer.Option(
            "--client-id",
            "-c",
            envvar=COMMAND_ENVVAR_PREFIX + "CLIENT_ID",
            prompt="API client_id",
            help="i.e.: papi-baaaaaad-c0de-fade-baad-00000000001d",
            hide_input=True,
        ),
    ],
    client_secret: Annotated[
        str,
        typer.Option(
            "--client-secret",
            "-p",
            envvar=COMMAND_ENVVAR_PREFIX + "CLIENT_SECRET",
            prompt="API client_secret",
            help="i.e.: verY-Secret-p4ssw0rd",
            hide_input=True,
        ),
    ],
    employee_id: Annotated[
        str,
        typer.Option(
            "--employee-id",
            "-i",
            envvar=COMMAND_ENVVAR_PREFIX + "EMPLOYEE_ID",
            prompt="Employee ID",
            help="i.e.: 123456",
        ),
    ],
) -> None:
    """Global options for personio commands."""

    PERSONIO_APP_STATE["auth_token"] = get_auth_token(client_id, client_secret)
    PERSONIO_APP_STATE["employee_id"] = employee_id


# Check personio api status
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
        error_and_exit("net_conn")


# Verify employee information
@app.command()
def employee() -> None:
    """Get my infomration from Personio."""

    access_token = PERSONIO_APP_STATE["auth_token"]
    employee_id = PERSONIO_APP_STATE["employee_id"]

    endpoint_url = "https://api.personio.de/v1/company/employees/" + employee_id
    headers = {"accept": "application/json", "authorization": f"Bearer {access_token}"}
    response = requests.get(endpoint_url, headers=headers)
    validate_http_status_code(response)
    validate_json_key("data", response.json())
    json_data = response.json()["data"]["attributes"]

    print_table_with_details(
        title="Employee Information",
        details=[
            ["Name", json_data["preferred_name"]["value"]],
            ["Email", json_data["email"]["value"]],
            ["Department", json_data["team"]["value"]["attributes"]["name"]],
            ["Company", json_data["subcompany"]["value"]["attributes"]["name"]],
            ["Status", json_data["status"]["value"]],
        ],
    )


# Create employee attendance
@app.command()
def attendance(
    attendance_date: Annotated[
        str,
        typer.Option(
            "--attendance-date",
            "-d",
            envvar=COMMAND_ENVVAR_PREFIX + "ATTENDANCE_DATE",
            help="i.e.: 2006-01-02",
        ),
    ] = "",
    attendance_weeks: Annotated[
        int,
        typer.Option(
            "--attendance-weeks",
            "-w",
            envvar=COMMAND_ENVVAR_PREFIX + "ATTENDANCE_WEEKS",
            help="i.e.: 4",
        ),
    ] = 0,
) -> None:
    """Create a single-day attendance."""

    access_token = PERSONIO_APP_STATE["auth_token"]
    employee_id = PERSONIO_APP_STATE["employee_id"]

    start_date = attendance_date or datetime.now().strftime("%Y-%m-%d")
    if attendance_weeks == 0:
        create_personio_attendance(access_token, employee_id, start_date)
    else:
        create_attendance_weeks = get_working_days_for_next_four_weeks(
            start_date, attendance_weeks
        )
        for i in create_attendance_weeks:
            create_personio_attendance(access_token, employee_id, i)
    typer.secho("Attendance added successfully.", fg=typer.colors.GREEN)
