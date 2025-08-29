"""This module provides project commands."""

# acli/project/app.py

import typer
from typing_extensions import Annotated

from acli.helpers import error_and_exit, run_cmd
from acli.configinit import get_app_config
from . import COMMAND_ENVVAR_PREFIX, DIRENV_FILE_CONTENT


app = typer.Typer()


@app.command()
def direnv() -> None:
    """Create a new direnv file in the current directory."""

    with open(".envrc", "w") as f:
        f.write(DIRENV_FILE_CONTENT)


@app.command()
def gitemail(
    work_email: Annotated[
        bool,
        typer.Option(
            "--work-email",
            "-w",
            envvar=COMMAND_ENVVAR_PREFIX + "WORK_EMAIL",
            help="i.e.: user@company.com",
        ),
    ] = False,
    personal_email: Annotated[
        bool,
        typer.Option(
            "--personal-email",
            "-p",
            envvar=COMMAND_ENVVAR_PREFIX + "PERSONAL_EMAIL",
            help="i.e.: user@personal.com",
        ),
    ] = False,
) -> None:
    """Set the git user email address."""

    email = ""
    if work_email and personal_email:
        error_and_exit(
            "app_input_conflict",
            "Both --personal-email and --work-email options cannot be provided.",
        )
    elif work_email:
        email = get_app_config("user.work_email")
    elif personal_email:
        email = get_app_config("user.personal_email")
    else:
        error_and_exit(
            "app_missing_input",
            "Either --personal-email or --work-email options must be provided.",
        )

    run_cmd(["git", "config", "user.email", email])
    typer.echo(f"Git user email set to: {email}")
