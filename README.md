# PiLibre

<!-- Cool ASCII logo? -->

<!-- Badges! -->

A small Python script for displaying hardware metrics. Metrics are pulled from LibreHardwareMonitor, and requires it to be installed on your PC and in server mode. It is designed to be run on a small computer with a small display. I intend to use a Raspberry Pi, but you could likely use something else.

<!-- Some examples will go here! -->

## Installation

PiLibre relies on `rich` and `httpx` on the display machine, and `LibreHardwareMonitor` on the machine from which you want to see metrics.

### Host Machine Setup

The host machine only needs to have LibreHardwareMonitor installed.
Once installed:

- Open the HTTP server via `Options -> HTTP Server`.
- Take note of the IP address. This is the IP address of the local machine.
- If you'd like to change the default port, do so here.

### Display Machine Setup

`pipx` is recommended for the simplest installation. This will install `PiLibre` into its own virtual environment, along with any dependencies.

If you know what you're doing, you can install the package via `Git` and run it manually, with `python -m src/pilibre`. As always, a virtual environment is recommended. Runtime dependencies can be installed with `python -m pip install requirements.txt`.

## Usage

Usage is very simple. Once the HTTP server is running on the host machine, simply specify the IP address and port in the config file and run the project.
