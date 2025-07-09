"""Top-level package for app CLI."""

# acli/__init__.py

__app_name__ = "acli"
__version__ = "0.2.1"

(
    SUCCESS,
    DEFAULT_ERROR,
    DIR_ERROR,
    FILE_ERROR,
    OS_COMMAND_ERROR,
    JSON_DATA_ERROR,
    NET_CONN_ERROR,
    HTTP_CODE_ERROR,
    APP_DOCKER_VAULT_ERROR,
) = range(9)

GLOBAL_ENVVAR_PREFIX = "ACLI_"
