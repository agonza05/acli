"""This module initializes project commands."""

# acli/project/__init__.py

from acli import GLOBAL_ENVVAR_PREFIX

COMMAND_ENVVAR_PREFIX = GLOBAL_ENVVAR_PREFIX + "PROJECT_"

DIRENV_FILE_CONTENT = """
dotenv_if_exists
source_up_if_exists
use sourceop
"""
