<p align="center">
    <img alt="PiLibre" src="https://github.com/acbuie/pilibre/blob/main/docs/assets/logo.svg"/>
</p>

<div align="center">
    <a href= "https://pypi.org/project/pilibre/">
        <img alt="PyPI - PiLibre Version" src="https://img.shields.io/pypi/v/pilibre?style=for-the-badge">
    </a>
    <a href="https://www.python.org/downloads/release/python-3110/">
        <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/pilibre?style=for-the-badge">
    </a>
    <a href="https://github.com/acbuie/pilibre/blob/main/LICENSE.txt">
        <img alt="License" src="https://img.shields.io/github/license/acbuie/pilibre?style=for-the-badge">
    </a>
</div>

<br/>

<div align="center">
    <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/acbuie/pilibre?style=for-the-badge">
    <a href="https://github.com/acbuie">
        <img alt="GitHub Profile" src="https://img.shields.io/static/v1?label=&message=Profile&style=for-the-badge&logo=github&labelColor=grey">
    </a>
</div>

A small Python script for displaying hardware metrics. Metrics are pulled from `LibreHardwareMonitor`, and requires it to be installed on your PC and in server mode. It is designed to be run on a small computer with a small display. I intend to use a Raspberry Pi, but you could likely use something else.

---

<!-- Some examples will go here! -->

## Installation

PiLibre relies on `rich` and `httpx` on the display machine, and `LibreHardwareMonitor` on the machine from which you want to see metrics.

- `rich`: For terminal display of the hardware metrics
- `httpx`: To pull the JSON data served by `LibreHardwareMonitor`
- `LibreHardwareMonitor`: For getting the hardware metrics of your computer.

### Host Machine Setup

The host machine only needs to have `LibreHardwareMonitor` installed. The project can be found here: https://github.com/LibreHardwareMonitor/LibreHardwareMonitor and downloaded from here: https://github.com/LibreHardwareMonitor/LibreHardwareMonitor/releases.

Once installed:

- Open the HTTP server via `Options -> HTTP Server`.
- Take note of the IP address. This is the IP address of the local machine.
- If you'd like to change the default port, do so here.

### Display Machine Setup

The machine you want to display metrics on needs to have the `PiLibre` application installed. The easiest way is to use `pipx`, but manual instructions are also included.

#### Via `pipx`

`pipx` is recommended for the simplest installation. This will install `PiLibre` into its own virtual environment, along with any dependencies.

Install `pipx` from here: https://github.com/pypa/pipx#install-pipx.

```shell
pipx install pilibre

# Or, via the repository on github
pipx install git+https://github.com/acbuie/pilibre.git
```

#### Via `pip`

You can also install manually via `pip`.

First, create a folder for the project.

```sh
mkdir pilibre
cd pilibre
```

Then, create and activate virtual environment for the project. A very basic setup is shown below.

You can read about virtual environments here: https://docs.python.org/3/tutorial/venv.html.

```sh
# Create virtual env with installed python
python -m venv .venv

# Activate
# On Mac/Linux:
source .venv/bin/activate

# On Windows:
venv/Scripts/activate.bat

# Then, install
python -m pip install pilibre
```

#### Via `git`

You can also install the package via `Git`. As always, a virtual environment is recommended, so the requirements don't get installed into the system python. Runtime dependencies can be installed with `python -m pip install requirements.txt`.

First, clone the project into a new directory.

```shell
mkdir pilibre
cd pilibre
git clone https://github.com/acbuie/pilibre.git
```

Once installed, create and activate a python virtual environment.

```sh
python -m venv .venv
source .venv/bin/activate
```

Then, install the dependencies.

```shell
python -m pip install requirements.txt
```

## Usage

Usage is very simple. Once the HTTP server is running on the host machine, simply specify the IP address and port in the config file and run the project.

Running the program depends on how it was installed.

- With `pipx`: `pilibre`
  - This works because `pipx` installs its programs onto the system PATH. These programs can be invoked from any directory in the shell.
- With `pip` or `git`: `python -m pilibre`
  - This requires you to run the above command in the directory in which you installed the project.

## Configuration

### Theming

### Layouts
