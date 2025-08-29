"""Helper functions."""

import typer
import subprocess
from typing import Any, List
from requests.models import Response
from rich.console import Console
from rich.table import Table

from . import ERROR_CODES, ERROR_MESSAGES


def error_and_exit(code: str = "default", message: str | None = None) -> None:
    """Helper to output error code and exit application."""

    if code not in ERROR_CODES:
        typer.secho(
            "Unkown Exit Code: This seems to be a bug. Please contact development team.",
            fg=typer.colors.RED,
        )
        raise typer.Exit(code=1)

    error_code = ERROR_CODES[code]
    error_message = ERROR_MESSAGES[code]
    if message:
        error_message = message
    typer.secho(f"Exit Code {error_code}: {error_message}", fg=typer.colors.RED)
    raise typer.Exit(code=error_code)


def run_cmd(cmd) -> str:
    """Helper to run commands in shell and returns stdout."""

    return_data = ""
    try:
        result = subprocess.run(cmd, text=True, capture_output=True, check=True)
        return_data = result.stdout.strip()
    except subprocess.CalledProcessError as e:
        error_and_exit("os_command", f"Running command {cmd} failed. {e.stderr}")
    return return_data


def validate_http_status_code(response: Response) -> None:
    """Helper validate and error on http status code."""

    if 300 >= response.status_code < 200:
        error_and_exit("http_code")


def validate_json_key(json_key: str, json_data: Any) -> None:
    """Helper validate and error on key existence."""

    if json_key not in json_data:
        error_and_exit("json_data", f"JSON key {json_key} not found.")


def print_table_with_details(title: str, details: List[List[str]]) -> None:
    """Helper to print table with details."""

    table = Table(title=title)
    table_row = []
    for detail in details:
        table.add_column(detail[0], justify="center")
        if detail[1] is None:
            detail_message = ""
        elif isinstance(detail[1], List):
            detail_message = ", ".join(detail[1])
        else:
            detail_message = detail[1]
        table_row.append(detail_message)

    table.add_row(*table_row)

    console = Console()
    console.print(table)
