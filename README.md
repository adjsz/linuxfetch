# linuxfetch

linuxfetch is a Linux CLI tool inspired by fastfetch for displaying hardware information and system info written in Python.

linuxfetch only works on Linux systems.

![image](examples/screenshot.png)

## Dependencies

linuxfetch uses the following dependencies:

```bash
pip install psutil
pip install rich
```

## Supported logos

As of now, linuxfetch only supports these distros in terms of logos:

- Linux Mint
- Debian
- Arch Linux
- Fedora Linux

If your distro is not apart of the following, a fallback logo will be used instead, which is the generic linux logo.

## Installation

For now, you can run this command in your linuxfetch folder:

```bash
git clone https://github.com/adjsz/linuxfetch.git
cd linuxfetch
python3 linuxfetch.py
```

Support for package managers such as `APT` will be added soon.