"""This module provides system commands."""

# acli/system/app.py

import typer
import platform
import psutil
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.console import Console
from rich.table import Table

from acli.helpers import run_cmd


app = typer.Typer()


@app.command()
def up() -> None:
    """Upgrade brew packages."""

    brew_commands = ["update", "upgrade", "cleanup"]

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        task = progress.add_task(
            description="[magenta]Updating packages...", total=len(brew_commands)
        )
        for command in brew_commands:
            progress.console.print(f" - brew {command}...")
            run_cmd(["brew", command])
            progress.advance(task)

    typer.secho("Packages upgraded successfully.", fg=typer.colors.GREEN)


@app.command()
def info() -> None:
    """Display system information."""

    console = Console()
    system_info = {}

    # Operating System details
    system_info["os"] = {
        "system": platform.system(),
        "node": platform.node(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
    }

    # CPU details
    system_info["cpu"] = {
        "physical_cores": psutil.cpu_count(logical=False),
        "total_cores": psutil.cpu_count(logical=True),
        "max_frequency": psutil.cpu_freq().max,
        "min_frequency": psutil.cpu_freq().min,
        "current_frequency": psutil.cpu_freq().current,
        "usage_per_core": psutil.cpu_percent(percpu=True),
        "total_usage": psutil.cpu_percent(),
    }

    # Memory details
    svmem = psutil.virtual_memory()
    system_info["memory"] = {
        "total": svmem.total,
        "available": svmem.available,
        "used": svmem.used,
        "percentage": svmem.percent,
    }

    # Disk details
    partitions = psutil.disk_partitions()
    disk_info = []
    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            disk_info.append(
                {
                    "device": partition.device,
                    "mountpoint": partition.mountpoint,
                    "fstype": partition.fstype,
                    "total": usage.total,
                    "used": usage.used,
                    "free": usage.free,
                    "percentage": usage.percent,
                }
            )
        except PermissionError:
            continue
    system_info["disk"] = disk_info

    # Printing system info
    for category, details in system_info.items():
        table = Table("Item", "Value", title=category.upper(), title_style="cyan")
        if isinstance(details, list):
            for item in details:
                for key, value in item.items():
                    table.add_row(key, str(value))
                table.add_section()
        else:
            for key, value in details.items():
                table.add_row(key, str(value))
        console.print(table)
