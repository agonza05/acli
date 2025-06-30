"""This module provides config init functionality."""

# acli/config/info.py

import typer

from acli import ERRORS, DIR_ERROR, FILE_ERROR, SUCCESS
from . import config_dir_path, config_file_path, env_file_path


app = typer.Typer()


def _init_config_file() -> int:
    """Helper function to create config files."""
    if not (env_file_path.exists() and config_file_path.exists()):
        try:
            config_dir_path.mkdir(exist_ok=True)
        except OSError:
            return DIR_ERROR
        try:
            config_file_path.touch(exist_ok=True, mode=0o644)
            env_file_path.touch(exist_ok=True, mode=0o600)
        except OSError:
            return FILE_ERROR
    return SUCCESS


def config_file() -> int:
    """Creates config files."""
    config_code = _init_config_file()
    if config_code != SUCCESS:
        return config_code
    return SUCCESS


@app.command()
def init() -> None:
    """Initializes configuration files."""
    config_init_error = config_file()
    if config_init_error:
        typer.secho(
            f'Creating config file failed with "{ERRORS[config_init_error]}"',
            fg=typer.colors.RED,
        )
        raise typer.Exit(1)
    else:
        typer.secho(
            f"The config files are in {str(config_dir_path)}", fg=typer.colors.GREEN
        )
