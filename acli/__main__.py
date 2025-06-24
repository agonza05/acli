"""App entry point script."""

# acli/__main__.py

from acli import cli, __app_name__


def main():
    cli.app(prog_name=__app_name__)


if __name__ == "__main__":
    main()
