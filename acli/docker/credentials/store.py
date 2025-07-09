"""This module provides docker credentials store functionality."""

# acli/docker/credentials/store.py

import typer
import sys
import json
from datetime import datetime

from acli.helpers import run_cmd
from . import VAULT_NAME_OPTION, DEFAULT_VAULT_NAME


app = typer.Typer()


@app.command()
def store(vault_name: VAULT_NAME_OPTION = DEFAULT_VAULT_NAME) -> None:
    """Show a credential from Docker credentials vault."""

    body = json.loads(sys.stdin.read())
    url = body["ServerURL"]
    username = body["Username"]
    credential = body["Secret"]
    result = run_cmd(["op", "item", "list", "--vault", vault_name, "--format", "json"])
    items = json.loads(result)
    existing = [i["id"] for i in items if i["title"] == url]
    fields = [
        f"username={username}",
        f"credential={credential}",
        f"valid from={int(datetime.now().timestamp())}",
        "expires=2147483647",
    ]

    if not existing:
        run_cmd(
            [
                "op",
                "item",
                "create",
                "--format",
                "json",
                "--title",
                url,
                "--category",
                "API Credential",
                "--vault",
                vault_name,
                "--",
            ]
            + fields
        )
    else:
        run_cmd(
            [
                "op",
                "item",
                "edit",
                "--format",
                "json",
                existing[0],
                "--vault",
                vault_name,
                "--",
            ]
            + fields
        )
