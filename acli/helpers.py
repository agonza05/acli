"""Helper functions."""

import typer
import subprocess
from typing import Any
from requests.models import Response

from . import DEFAULT_ERROR, OS_COMMAND_ERROR, HTTP_CODE_ERROR, JSON_DATA_ERROR


def error_and_exit(
    error_code: int = DEFAULT_ERROR, error_msg: str | None = None
) -> None:
    """Helper to output error code and exit application."""

    msg = "An error occured. Exiting app..."
    if error_msg:
        msg = error_msg
    typer.secho(f"Error {error_code}: {msg}", fg=typer.colors.RED)
    raise typer.Exit()


def run_cmd(cmd) -> str:
    """Helper to run commands in shell and returns stdout."""

    return_data = ""
    try:
        result = subprocess.run(cmd, text=True, capture_output=True, check=True)
        return_data = result.stdout.strip()
    except subprocess.CalledProcessError as e:
        error_and_exit(OS_COMMAND_ERROR, f"Running command {cmd} failed. {e.stderr}")
    return return_data


def validate_http_status_code(response: Response) -> None:
    """Helper validate and error on http status code."""

    if 300 >= response.status_code < 200:
        error_and_exit(HTTP_CODE_ERROR, "Response has not a HTTP 2XX status code.")


def validate_json_key(json_key: str, json_data: Any) -> None:
    """Helper validate and error on key existence."""

    if json_key not in json_data:
        error_and_exit(JSON_DATA_ERROR, f"JSON key {json_key} not found.")
