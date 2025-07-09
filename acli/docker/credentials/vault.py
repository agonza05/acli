"""This module provides dockercreds get functionality."""

# acli/dockercreds/info.py

import typer
import json

from acli.helpers import run_cmd
from . import VAULT_NAME_OPTION, DEFAULT_VAULT_NAME


app = typer.Typer()


def get_vault(vault_name: str) -> dict:
    """Get 1password vault."""

    result = run_cmd(["op", "vault", "list", "--format", "json"])
    vaults = json.loads(result)
    vault_data = [vault for vault in vaults if vault["name"] == vault_name]
    if len(vault_data) > 1:
        typer.secho(
            "Warning: Multiple vaults found. Using the first vault retrieved.",
            fg=typer.colors.YELLOW,
        )
    elif len(vault_data) == 0:
        typer.secho(
            f'Vault "{vault_name}" not found.',
            fg=typer.colors.RED,
        )
        raise typer.Exit()
    return vault_data[0]


@app.command()
def vault(vault_name: VAULT_NAME_OPTION = DEFAULT_VAULT_NAME) -> None:
    """Show 1password vault information used by Docker."""

    vault = get_vault(vault_name)
    typer.echo(f"Vault ID: {vault['id']}")
    typer.echo(f"Name: {vault['name']}")
    typer.echo(f"Number of Items: {vault['items']}")
