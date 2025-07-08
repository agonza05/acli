"""This module provides dockercreds get functionality."""

# acli/dockercreds/info.py

import typer
import subprocess
import sys


app = typer.Typer()


@app.command()
def vault() -> None:
    registry = sys.stdin.read().strip()
    result = subprocess.run(
        ["op", "vault", "list", "--format", "json"],
        text=True,
        capture_output=True,
        check=True,
    )
    print(result.stdout)
    print(registry)
