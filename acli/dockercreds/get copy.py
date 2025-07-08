"""This module provides dockercreds get functionality."""

# acli/dockercreds/info.py

import typer
import json
from typing_extensions import Annotated

from . import (
    COMMAND_ENVVAR_PREFIX,
)

app = typer.Typer()


class DockerCred:
    Username: str
    Secret: str
    ServerURL: str


# @app.command()
# def get(
#     url: Annotated[
#         str,
#         typer.Argument(
#             envvar=COMMAND_ENVVAR_PREFIX + "URL",
#         ),
#     ]
# ) -> None:
#     """Upgrade brew packages."""

#     test = DockerCred()
#     test.Username = "Testing"
#     test.Secret = "Testing1"
#     test.ServerURL = url

#     json_data = json.dumps(test.__dict__)
#     typer.echo(json_data)

# for command in commands:
#     result = subprocess.run(command, shell=True)
#     if result.returncode != 0:
#         typer.secho(
#             f"Attendance posting failed. Error {ERRORS[OS_COMMAND_ERROR]}",
#             fg=typer.colors.RED,
#         )
#         raise typer.Exit()
# typer.secho("Packages upgraded successfully.", fg=typer.colors.GREEN)
