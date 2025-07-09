"""This module provides docker credentials list functionality."""

# acli/docker/credentials/list.py

import typer
import json

from acli.helpers import run_cmd
from . import VAULT_NAME_OPTION, DEFAULT_VAULT_NAME


app = typer.Typer()


@app.command()
def list(vault_name: VAULT_NAME_OPTION = DEFAULT_VAULT_NAME) -> None:
    """List all credentials from Docker credentials vault."""

    result = run_cmd(
        ["op", "item", "list", "--vault", vault_name, "--format", "json"]
    )
    json_data = json.loads(result)
    output = {}
    for item in json_data:
        item_data = run_cmd(
            ["op", "item", "get", item["id"], "--vault", vault_name, "--format", "json"]
        )
        if item_data:
            json_item_data = json.loads(item_data)
            title = f"{json_item_data['title']}"
            fields = {f["id"]: f["value"] for f in json_item_data.get("fields", []) if any(value == f["id"] for value in ["username", "credential"]) }
            output[title] = fields.get("username")

    typer.echo(json.dumps(output))
