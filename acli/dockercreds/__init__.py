"""This module initializes dockercreds commands."""

# acli/dockercreds/__init__.py

from acli import GLOBAL_ENVVAR_PREFIX

COMMAND_ENVVAR_PREFIX = GLOBAL_ENVVAR_PREFIX + "DOCKERCREDS_"
DOCKER_1PASSWORD_VAULT = "Docker Credential Helper"


class DockerCred:
    Username: str
    Secret: str
    ServerURL: str
