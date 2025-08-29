"""This module provides config commands."""

# acli/config/app.py

import os
import typer
import configparser
from typing_extensions import Annotated

from acli import GLOBAL_ENVVAR_PREFIX
from acli.configinit import (
    config_dir_path,
    config_file_path,
    CONFIG_FILE_NAME,
    ENV_FILE_NAME,
)
from acli.helpers import error_and_exit

app = typer.Typer()


@app.command()
def show() -> None:
    """Show app configuration."""

    with open(config_file_path, "r") as file:
        file_content = file.read()
        typer.echo(file_content)


@app.command()
def env() -> None:
    """Show envrionment variables."""

    for key, value in os.environ.items():
        if key.startswith(GLOBAL_ENVVAR_PREFIX):
            typer.echo(f"{key}={value}")


@app.command()
def path() -> None:
    """Display full path of configuration files."""

    typer.echo(
        f"Configuration files are located in: {str(config_dir_path)}",
    )
    typer.echo(
        f"App configuration is taken from: {CONFIG_FILE_NAME}",
    )
    typer.echo(
        f"Envrionment variables are sourced from: {ENV_FILE_NAME}",
    )


@app.command()
def set(
    key_path: Annotated[
        str,
        typer.Option(
            "--key-path",
            "-p",
            prompt="Section path and key",
            help="i.e.: section.subsection.key",
        ),
    ],
    key_value: Annotated[
        str,
        typer.Option(
            "--key-value",
            "-v",
            prompt="Key value to update",
            help="i.e.: new_value",
        ),
    ],
) -> None:
    """Set app configuration."""

    config_parser = configparser.ConfigParser()
    config_parser.read(config_file_path)

    path_parts = key_path.split(".")
    if len(path_parts) < 2:
        error_and_exit(
            "config_key_path",
            "key_path must be of the form section[.subsection...].key",
        )

    # The key is always the last part
    key = path_parts[-1]
    # Section name is the rest joined by '.'
    section = ".".join(path_parts[:-1])

    # If section doesn't exist, add it
    if not config_parser.has_section(section):
        config_parser.add_section(section)

    config_parser.set(section, key, key_value)

    with open(config_file_path, "w") as file:
        config_parser.write(file)
