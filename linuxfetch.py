import platform
import socket
import psutil
import subprocess
import getpass
import os
from rich.console import Console

console = Console(highlight=False)

mem = psutil.virtual_memory()
disk = psutil.disk_usage("/")
GB = 1024**3 # converts bytes into gb

username = getpass.getuser()
info = platform.freedesktop_os_release()
architecture = platform.machine()

hostname = socket.gethostname()
logical_cores = psutil.cpu_count(logical=True)
physical_cores = psutil.cpu_count(logical=False)
cpu_usage = psutil.cpu_percent(interval=1)


full_name = f"{username}@{hostname}"

def show_os():
    console.print(f"{'[bold red]OS:[/bold red]         ':<12}{info['PRETTY_NAME']} {architecture}")

def show_hostname():
    console.print(f"[bold red]Hostname:[/bold red]   {hostname:<12}")

def show_logical_cores():
    console.print(f"[bold red]Threads:[/bold red]    {logical_cores:<12}")

def show_physical_cores():
    console.print(f"[bold red]Cores:[/bold red]      {physical_cores:<12}")

def show_cpu_usage():
    console.print(f"[bold red]CPU Usage:[/bold red]  {cpu_usage} %")

def show_total_ram():
    console.print(f"{'[bold red]Total RAM:[/bold red]  ':<12}{round(mem.total / GB, 2)} GB")

def show_used_ram():
    console.print(f"{'[bold red]Used RAM:[/bold red]   ':<12}{round(mem.used / GB, 2)} GB")

def show_disk_total():
    console.print(f"{'[bold red]Disk Total:[/bold red] ':<12}{round(disk.total / GB, 2)} GB")

def show_disk_free():
    console.print(f"{'[bold red]Disk Free:[/bold red]  ':<12}{round(disk.free / GB, 2)} GB")

def get_cpu_name():
    with open("/proc/cpuinfo") as f:
        for line in f:
            if "model name" in line:
                return line.split(":")[1].strip()
        return "CPU not found"

def show_cpu():
    console.print(f"{'[bold red]CPU:[/bold red]        ':<12}{get_cpu_name()}", overflow="ignore")

def get_gpu_name():
    try:
        result = subprocess.check_output(["lspci"], text=True)
        for line in result.splitlines():
            if "VGA" in line or "3D controller" in line:
                gpu_full = line.split("controller:", 1)[1].strip() # actual full name of gpu
                gpu_name = gpu_full.split("(")[0].strip() # removes (rev) bit to make it look cleaner
                return gpu_name
    except FileNotFoundError:
        return "lspci not found"
    return "GPU not found"

def show_gpu():
    console.print(f"{'[bold red]GPU:[/bold red]        ':<12}{get_gpu_name()}", overflow="ignore")


def show_logo():
    os_info = platform.system().lower()
    logo_file = None

    script_dir = os.path.dirname(os.path.abspath(__file__))

    if "linux" in os_info:
        distro_name = platform.freedesktop_os_release().get("PRETTY_NAME", "").lower()

        if "mint" in distro_name:
            logo_file = os.path.join(script_dir, "logos", "mint.txt") # Linux Mint
        elif "debian" in distro_name:
            logo_file = os.path.join(script_dir, "logos", "debian.txt") # Linux Debian
        else:
            logo_file = os.path.join(script_dir, "logos", "tux.txt") # Fallback if it cannot find the distro
    else:
        console.print("[bold red]Error:[/bold red] OS is not supported, only Linux is supported") # Error if user does not have a Linux OS
        return

    try:
        with open(logo_file, "r", encoding="utf-8") as f:
            logo = f.read()
        console.print(logo)
    except FileNotFoundError:
        console.print("[bold red]Error:[/bold red] Logo file not found")


def show_specs():
    show_logo()
    console.print(f"[bold red]{full_name.split('@')[0]}[/bold red]@[bold red]{full_name.split('@')[1]}[/bold red]")
    print('---------------')
    show_os()
    show_hostname()
    show_cpu()
    show_physical_cores()
    show_logical_cores()
    show_cpu_usage()
    show_gpu()
    show_total_ram()
    show_used_ram()
    show_disk_total()
    show_disk_free()

def main():
    show_specs()

main()