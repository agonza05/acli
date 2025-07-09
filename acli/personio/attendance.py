"""This module provides personio attendance."""

# acli/personio/attendance.py

import typer
import requests
from datetime import datetime, timedelta
from typing import List
from typing_extensions import Annotated

from acli.helpers import validate_http_status_code
from . import (
    COMMAND_ENVVAR_PREFIX,
    PERSONIO_BASE_URL,
    CLIENT_ID_OPTIONS,
    CLIENT_SECRET_OPTIONS,
    EMPLOYEE_ID_OPTIONS,
)
from .auth import get_auth_token

DEFAULT_START_TIME = {
    "MORNING": "08:30:00",
    "AFTERNOON": "13:00:00",
}
DEFAULT_END_TIME = {
    "MORNING": "12:30:00",
    "AFTERNOON": "17:00:00",
}

app = typer.Typer()


def _attendance(access_token: str, employee_id: str, start_date: str) -> None:
    """Helper function to create a single-day attendance."""

    endpoint_url = PERSONIO_BASE_URL + "/attendance-periods?skip_approval=true"
    headers = {
        "accept": "application/json",
        "Beta": "true",
        "content-type": "application/json",
        "authorization": "Bearer " + access_token,
    }
    for item in list(DEFAULT_START_TIME.keys()):
        payload = {
            "person": {"id": employee_id},
            "type": "WORK",
            "start": {"date_time": start_date + "T" + DEFAULT_START_TIME[item]},
            "end": {"date_time": start_date + "T" + DEFAULT_END_TIME[item]},
        }
        response = requests.post(endpoint_url, headers=headers, json=payload)
        validate_http_status_code(response)


def get_working_days_for_next_four_weeks(start_date: str, weeks: int) -> List[str]:
    """Return the working days for the following 4 weeks starting from the previous Monday."""

    req_date = datetime.strptime(start_date, "%Y-%m-%d")
    # Find the previous Monday
    last_monday = req_date - timedelta(days=req_date.weekday())

    # Generate working days for the next 4 weeks
    working_days = []
    for week in range(weeks):
        week_start = last_monday + timedelta(weeks=week)
        for day in range(5):  # Monday to Friday
            work_day = week_start + timedelta(days=day)
            working_days.append(work_day.strftime("%Y-%m-%d"))

    return working_days


@app.command()
def attendance(
    client_id: CLIENT_ID_OPTIONS,
    client_secret: CLIENT_SECRET_OPTIONS,
    employee_id: EMPLOYEE_ID_OPTIONS,
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

    access_token = get_auth_token(client_id, client_secret)
    start_date = attendance_date or datetime.now().strftime("%Y-%m-%d")
    if attendance_weeks == 0:
        _attendance(access_token, employee_id, start_date)
    else:
        create_attendance_weeks = get_working_days_for_next_four_weeks(
            start_date, attendance_weeks
        )
        for i in create_attendance_weeks:
            _attendance(access_token, employee_id, i)
    typer.secho("Attendance added successfully.", fg=typer.colors.GREEN)
