"""Helper function that run commands in shell."""

import typer
import subprocess

from acli import ERRORS, OS_COMMAND_ERROR


def run_cmd(cmd) -> str:
    try:
        result = subprocess.run(cmd, text=True, capture_output=True, check=True)
        if result.returncode != 0:
            typer.secho(
                f"Running command {cmd} failed. Error {ERRORS[OS_COMMAND_ERROR]}",
                fg=typer.colors.RED,
            )
            raise typer.Exit()
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return e.output
