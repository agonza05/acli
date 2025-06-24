import typer

from .info import app as info_app

app = typer.Typer()

app.add_typer(info_app)
