"""This module initializes config commands."""

# acli/config/__init__.py

import typer
from pathlib import Path
from acli import GLOBAL_ENVVAR_PREFIX, __app_name__

COMMAND_ENVVAR_PREFIX = GLOBAL_ENVVAR_PREFIX + "CONFIG_"
CONFIG_FILE_NAME = "config.ini"
ENV_FILE_NAME = ".env"

config_dir_path = Path(typer.get_app_dir(__app_name__))
config_file_path = config_dir_path / CONFIG_FILE_NAME
env_file_path = config_dir_path / ENV_FILE_NAME
