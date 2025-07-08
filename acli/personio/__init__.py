"""This module initializes personio commands."""

# acli/personio/__init__.py

import typer
from typing_extensions import Annotated

from acli import GLOBAL_ENVVAR_PREFIX

COMMAND_ENVVAR_PREFIX = GLOBAL_ENVVAR_PREFIX + "PERSONIO_"
PERSONIO_BASE_URL = "https://api.personio.de/v2"
PERSONIO_STATUS_URL = "https://status.personio.de/api/v2/status.json"

CLIENT_ID_OPTIONS = Annotated[
    str,
    typer.Option(
        "--client-id",
        "-c",
        envvar=COMMAND_ENVVAR_PREFIX + "CLIENT_ID",
        prompt="API client_id",
        help="i.e.: papi-baaaaaad-c0de-fade-baad-00000000001d",
        hide_input=True,
    ),
]

CLIENT_SECRET_OPTIONS = Annotated[
    str,
    typer.Option(
        "--client-secret",
        "-p",
        envvar=COMMAND_ENVVAR_PREFIX + "CLIENT_SECRET",
        prompt="API client_secret",
        help="i.e.: verY-Secret-p4ssw0rd",
        hide_input=True,
    ),
]

EMPLOYEE_ID_OPTIONS = Annotated[
    str,
    typer.Option(
        "--employee-id",
        "-i",
        envvar=COMMAND_ENVVAR_PREFIX + "EMPLOYEE_ID",
        prompt="Employee ID",
        help="i.e.: 123456",
    ),
]
