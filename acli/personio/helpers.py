"""This module provides personio helpers functionality."""

# acli/personio/helpers.py

from typing import List
import requests
from datetime import datetime, timedelta

from acli.helpers import error_and_exit, validate_http_status_code, validate_json_key
from . import PERSONIO_BASE_URL


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
        error_and_exit("net_conn", f"API request error. {e.strerror}")
    return return_data


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


def create_personio_attendance(
    access_token: str, employee_id: str, start_date: str
) -> None:
    """Helper function to create a single-day attendance."""

    DEFAULT_START_TIME = {
        "MORNING": "08:30:00",
        "AFTERNOON": "13:00:00",
    }
    DEFAULT_END_TIME = {
        "MORNING": "12:30:00",
        "AFTERNOON": "17:00:00",
    }

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
