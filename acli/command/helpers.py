"""This module provides helper functions forcommand commands."""

# acli/command/helpers.py

import os


def generate_command_files(command_name: str) -> None:
    """
    Create a directory named as 'command_name' and an app.py file in it with customized content.
    """

    APP_FILE_NAME = "app.py"
    app_file_content = f'''
"""This module provides {command_name} commands."""

# acli/{command_name}/app.py

import typer

app = typer.Typer()
'''

    dir_name = command_name
    file_path = os.path.join(dir_name, APP_FILE_NAME)
    os.makedirs(dir_name, exist_ok=True)

    with open(file_path, "w") as f:
        f.write(app_file_content)
