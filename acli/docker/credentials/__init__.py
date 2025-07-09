"""This module initializes docker credentials commands."""

# acli/docker/credentials/__init__.py

import typer
from typing_extensions import Annotated

from acli.docker import COMMAND_ENVVAR_PREFIX

DEFAULT_VAULT_NAME = "Docker"

VAULT_NAME_OPTION = Annotated[
    str,
    typer.Option(
        "--vault-name",
        "-v",
        envvar=COMMAND_ENVVAR_PREFIX + "VAULT_NAME",
        help="i.e.: Docker",
    ),
]


class DockerCred:
    Username: str
    Secret: str
    ServerURL: str
