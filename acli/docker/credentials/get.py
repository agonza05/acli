"""This module provides docker credentials get functionality."""

# acli/docker/credentials/get.py

import typer
import sys
import json

from acli.helpers import run_cmd
from . import VAULT_NAME_OPTION, DEFAULT_VAULT_NAME


app = typer.Typer()


@app.command()
def get(vault_name: VAULT_NAME_OPTION = DEFAULT_VAULT_NAME) -> None:
    """Show a credential from Docker credentials vault."""

    registry = sys.stdin.read().strip()
    result = run_cmd(
        ["op", "item", "get", registry, "--vault", vault_name, "--format", "json"]
    )
    json_data = json.loads(result)
    fields = {
        f["id"]: f["value"]
        for f in json_data.get("fields", [])
        if any(value == f["id"] for value in ["username", "credential"])
    }
    output = {
        "ServerURL": registry,
        "Username": fields.get("username"),
        "Secret": fields.get("credential"),
    }
    typer.echo(json.dumps(output))
