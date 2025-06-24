"""This module provides the app CLI."""

# acli/cli.py

# from pathlib import Path
from typing import Optional
import typer

from acli import ERRORS, __app_name__, __version__, config
from .system import app as sys_app

app = typer.Typer()

app.add_typer(sys_app, name="system", help="System commands.")


@app.command()
def init() -> None:
    """Initialize the app."""
    app_init_error = config.init_app()
    if app_init_error:
        typer.secho(
            f'Creating config file failed with "{ERRORS[app_init_error]}"',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    else:
        typer.secho(
            f"The config file is {str(config.CONFIG_FILE_PATH)}", fg=typer.colors.GREEN
        )


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return
