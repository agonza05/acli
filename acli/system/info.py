import typer
import platform
import psutil
from rich.console import Console
from rich.table import Table

console = Console()
app = typer.Typer()


def get_system_info():
    info = {}

    # Operating System details
    info["os"] = {
        "system": platform.system(),
        "node": platform.node(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
    }

    # CPU details
    info["cpu"] = {
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
    info["memory"] = {
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
    info["disk"] = disk_info

    return info


@app.command()
def info() -> None:
    """Display system information."""
    system_info = get_system_info()
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
