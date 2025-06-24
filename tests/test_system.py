# tests/test_acli.py

import re
from typer.testing import CliRunner


from acli import cli

runner = CliRunner()


SYSTEM_INFO_CATEGORIES = ["OS","CPU", "MEMORY", "DISK"]
REGEX_PATTERN = "^\\s*(" + "|".join(SYSTEM_INFO_CATEGORIES) + ")\\s*\n"

def test_system_info():
    result = runner.invoke(cli.app, ["system", "info"])
    assert result.exit_code == 0
    pattern = re.compile(REGEX_PATTERN, re.MULTILINE)
    matches = pattern.findall(result.stdout)
    assert matches == SYSTEM_INFO_CATEGORIES
