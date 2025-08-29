"""Top-level package for app CLI."""

# acli/__init__.py

__app_name__ = "acli"
__version__ = "0.1.0"

APP_STATE = {}

GLOBAL_ENVVAR_PREFIX = "ACLI_"

ERROR_CODES = dict(
    success=0,
    default=1,
    directory=2,
    file=3,
    os_command=4,
    json_data=5,
    net_conn=6,
    http_code=7,
    config_key_path=8,
    app_missing_input=101,
    app_input_conflict=102,
    app_docker_vault=103,
)

ERROR_MESSAGES = dict(
    success="Success",
    default="An error occured. Exiting app...",
    directory="Directory does not exist or could not be created.",
    file="File does not exist or could not be created.",
    os_command="OS command failed.",
    json_data="JSON data is invalid.",
    net_conn="Network connection failed.",
    http_code="HTTP response code is not 200.",
    config_key_path="Config key path is invalid.",
    app_missing_input="User input is missing.",
    app_input_conflict="User input is conflicting.",
    app_docker_vault="Docker Vault does not exist.",
)
