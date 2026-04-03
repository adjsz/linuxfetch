# linuxfetch

linuxfetch is a Linux CLI tool inspired by fastfetch for displaying hardware information and system info written in Python.

linuxfetch only works on Linux systems.

![image](examples/screenshot.png)

## Dependencies

linuxfetch uses the following dependencies:

### Using pip:

```bash
pip install psutil
pip install rich
```

### For Debian-based distros that have externally-managed environments:
```bash
sudo apt install python3-psutil
sudo apt install python3-rich
```

## Supported distros

As of now, linuxfetch only supports these distros:

- Linux Mint
- Debian
- Arch Linux
- Fedora Linux

If your distro is not apart of the following, a fallback logo will be used instead, which is the generic linux logo.

### Note:

Logos are stored in .txt folders in the folders folder.

Right now, there is no way for you to use your own logos that doesn't include you modifying the source code.

## Installation

For now, you can run this command in your linuxfetch folder:

```bash
git clone https://github.com/adjsz/linuxfetch.git
cd linuxfetch
python3 linuxfetch.py
```

Support for package managers such as APT` will be added soon.