"""This module provides docker credentials erase functionality."""

# acli/docker/credentials/erase.py

import typer
import sys
import json

from acli.helpers import run_cmd
from . import VAULT_NAME_OPTION, DEFAULT_VAULT_NAME


app = typer.Typer()


@app.command()
def erase(vault_name: VAULT_NAME_OPTION = DEFAULT_VAULT_NAME) -> None:
    """Erase a credential from Docker credentials vault."""

    registry = sys.stdin.read().strip()
    result = run_cmd(
        ["op", "item", "get", registry, "--vault", vault_name, "--format", "json"]
    )
    json_data = json.loads(result)
    if result:
        run_cmd(
            ["op", "item", "delete", json_data["id"], "--vault", vault_name]
        )
