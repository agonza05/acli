"""Top-level package for app CLI."""

# acli/__init__.py

__app_name__ = "acli"
__version__ = "0.1.0"

(
    SUCCESS,
    DIR_ERROR,
    FILE_ERROR,
    DB_READ_ERROR,
    DB_WRITE_ERROR,
    JSON_ERROR,
    ID_ERROR,
    CONN_ERROR,
    API_GET_ERROR,
    API_POST_ERROR,
    OS_COMMAND_ERROR,
) = range(11)

ERRORS = {
    DIR_ERROR: "config directory error",
    FILE_ERROR: "config file error",
    DB_READ_ERROR: "database read error",
    DB_WRITE_ERROR: "database write error",
    ID_ERROR: "app id error",
    CONN_ERROR: "connection error",
    API_GET_ERROR: "api post error",
    API_POST_ERROR: "api post error",
    OS_COMMAND_ERROR: "OS command error",
}

GLOBAL_ENVVAR_PREFIX = "ACLI_"
