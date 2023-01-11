"""This module loads the PiLibre configuration."""


import os
from pathlib import Path

_FILE_NAME = "pilibre.toml"
_DIR_NAME = "pilibre"


def _get_config_file(directory: Path) -> Path | None:
    config_file = directory / _FILE_NAME

    if config_file.exists() and config_file.is_file():
        return config_file

    return None


def find_config() -> Path:
    """Get the path to the user configuration file.

    Log all the config files that are found.

    Raises:
        FileNotFoundError: Raised if no configuration file is found.

    Returns:
        Path: Path to configuration file.
    """
    xdg_config = Path(os.environ["XDG_CONFIG_HOME"]) / _DIR_NAME
    dot_config = Path().home() / ".config" / _DIR_NAME

    configs = []

    if xdg_config_file := _get_config_file(xdg_config):
        configs.append(xdg_config_file)

    if dot_config_file := _get_config_file(dot_config):
        configs.append(dot_config_file)

    if not configs:
        raise FileNotFoundError("No configuration file found.")

    # TODO: log paths to all config files found

    # Only return the first found
    return configs[0]
