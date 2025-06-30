#!/usr/bin/env bash

source .venv/bin/activate
rm README.md
touch README.md
typer acli.main utils docs --name "acli" >> README.md
typer acli.system.app utils docs --name "acli system" >> README.md
typer acli.config.app utils docs --name "acli config" >> README.md
typer acli.personio.app utils docs --name "acli personio" >> README.md
