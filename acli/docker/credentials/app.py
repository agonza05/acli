"""This module provides docker credentials commands."""

# acli/docker/credentials/app.py

import typer

from .vault import app as vault_app
from .get import app as get_app
from .erase import app as erase_app
from .list import app as list_app
from .store import app as store_app

app = typer.Typer()

app.add_typer(vault_app)
app.add_typer(get_app)
app.add_typer(erase_app)
app.add_typer(list_app)
app.add_typer(store_app)
