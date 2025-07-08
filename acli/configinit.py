"""Initializes app config."""

# acli/init.py

import typer
from pathlib import Path
from dotenv import load_dotenv

from . import __app_name__, DIR_ERROR, FILE_ERROR
from .helpers import error_and_exit

CONFIG_FILE_NAME = "config.ini"
ENV_FILE_NAME = ".env"

config_dir_path = Path(typer.get_app_dir(__app_name__))
config_file_path = config_dir_path / CONFIG_FILE_NAME
env_file_path = config_dir_path / ENV_FILE_NAME


def load_env_vars() -> None:
    """Helper to load envrionment variables."""

    load_dotenv(dotenv_path=env_file_path)


def init_config() -> None:
    """Initializes config files."""
    if not (env_file_path.exists() and config_file_path.exists()):
        try:
            config_dir_path.mkdir(exist_ok=True)
        except OSError:
            error_and_exit(DIR_ERROR, "Creating config directory failed.")
        try:
            config_file_path.touch(exist_ok=True, mode=0o644)
            env_file_path.touch(exist_ok=True, mode=0o600)
        except OSError:
            error_and_exit(FILE_ERROR, "Creating config directory failed.")
        typer.secho(
            f"Init: Config files location: {str(config_dir_path)}", fg=typer.colors.BLUE
        )
