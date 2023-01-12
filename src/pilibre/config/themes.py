"""This module finds the built in color themes."""

from configparser import ConfigParser
from pathlib import Path
from typing import Literal

from rich.terminal_theme import TerminalTheme

from pilibre._color import color_to_rgb


def find_built_in_themes(theme_type: Literal["display", "terminal"]) -> list[Path]:
    """Finds the paths to the built in themes.

    Args:
        type (Literal['display', 'terminal']): Get the display themes or
        the terminal themes.

    Returns:
        list[Path]: Path to themes.
    """
    if theme_type == "display":
        path_stub = Path("themes/display")
    elif theme_type == "terminal":
        path_stub = Path("themes/terminal")
    else:
        raise ValueError("Invalid theme_type passed.")

    # Path to themes folder in pilibre
    pilibre_path = Path(__file__).parent.parent.joinpath(path_stub).resolve()

    themes = [theme for theme in pilibre_path.iterdir()]

    return themes


def terminal_theme_from_file(file: Path) -> TerminalTheme:
    """Create a terminal theme from a file.

    Args:
        file (Path): File path to the theme file.

    Raises:
        FileNotFoundError: Raised if theme is not found. Likely to be
        swtiched to a log error, instead of raising an exception. # TODO

    Returns:
        TerminalTheme: A terminal theme.
    """
    config = ConfigParser()
    if not config.read(file):
        raise FileNotFoundError("Terminal theme not found!")

    basic = [*dict(config["basic"]).values()]
    standard = [*dict(config["standard"]).values()]
    bright = [*dict(config["bright"]).values()]

    basic_rgb = [color_to_rgb(rgb) for rgb in basic]
    standard_rgb = [color_to_rgb(rgb) for rgb in standard]
    bright_rgb = [color_to_rgb(rgb) for rgb in bright]

    theme = TerminalTheme(
        basic_rgb[0],
        basic_rgb[1],
        standard_rgb,
        bright_rgb,
    )

    return theme
