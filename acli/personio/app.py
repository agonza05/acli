"""This module provides personio commands."""

# acli/personio/app.py

import typer

from .status import app as status_app
from .auth import app as auth_app
from .employee import app as employee_app
from .attendance import app as attendance_app


app = typer.Typer()

app.add_typer(status_app)
app.add_typer(auth_app)
app.add_typer(employee_app)
app.add_typer(attendance_app)
