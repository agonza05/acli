"""This module initializes personio commands."""

# acli/personio/__init__.py

from acli import GLOBAL_ENVVAR_PREFIX, APP_STATE

PERSONIO_APP_STATE = APP_STATE["personio"] = {}

COMMAND_ENVVAR_PREFIX = GLOBAL_ENVVAR_PREFIX + "PERSONIO_"
PERSONIO_BASE_URL = "https://api.personio.de/v2"
PERSONIO_STATUS_URL = "https://status.personio.de/api/v2/status.json"
