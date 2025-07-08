# tests/test_acli.py

import re
from typer.testing import CliRunner


from acli import cli

runner = CliRunner()


SYSTEM_INFO_CATEGORIES = ["OS", "CPU", "MEMORY", "DISK"]
REGEX_PATTERN = r"^\s*(" + "|".join(SYSTEM_INFO_CATEGORIES) + r")\s*\n"


def test_system_info():
    result = runner.invoke(cli.app, ["system", "info"])
    assert result.exit_code == 0
    matches = re.findall(REGEX_PATTERN, result.stdout, re.MULTILINE)
    assert matches == SYSTEM_INFO_CATEGORIES


def test_system_up():
    expected_lines = ["Packages upgraded successfully."]
    result = runner.invoke(cli.app, ["system", "up"])
    assert result.exit_code == 0
    for line in expected_lines:
        assert line in result.stdout
