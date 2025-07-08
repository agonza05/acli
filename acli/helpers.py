"""Helper functions."""

import typer
import subprocess
from requests.models import Response

from . import DEFAULT_ERROR, OS_COMMAND_ERROR, HTTP_CODE_ERROR


def error_and_exit(
    error_code: int = DEFAULT_ERROR, error_msg: str | None = None
) -> None:
    """Helper to output error code and exit application."""

    msg = "An error occured. Exiting app..."
    if error_msg:
        msg = error_msg
    typer.secho(f"Error {error_code}: {msg}", fg=typer.colors.RED)
    raise typer.Exit()


def run_cmd(cmd) -> str | None:
    """Helper to run commands in shell and returns stdout."""

    try:
        result = subprocess.run(cmd, text=True, capture_output=True, check=True)
        if result.returncode != 0:
            error_and_exit(OS_COMMAND_ERROR, f"Running command {cmd} failed.")
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        error_and_exit(
            OS_COMMAND_ERROR, f"Trying to run command {cmd} failed. {e.stderr}"
        )


def validate_http_status_code(response: Response) -> None:
    """Helper validate and error on http status code."""

    if 300 >= response.status_code < 200:
        error_and_exit(HTTP_CODE_ERROR, "Response has not a HTTP 2XX status code.")
