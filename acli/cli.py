"""This module provides the app CLI."""

# acli/cli.py

from typing import Optional
import typer

from acli import __app_name__, __version__
from .config.app import app as config_app
from .system.app import app as sys_app
from .personio.app import app as personio_app

app = typer.Typer()

app.add_typer(config_app, name="config", help="Config commands.")
app.add_typer(sys_app, name="system", help="System commands.")
app.add_typer(personio_app, name="personio", help="Personio commands.")


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
