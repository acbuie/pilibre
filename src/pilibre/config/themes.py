"""This module finds the built in color themes."""

from configparser import ConfigParser
from pathlib import Path
from typing import Literal

from rich.terminal_theme import DEFAULT_TERMINAL_THEME, TerminalTheme

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

    basic_rgb = [color_to_rgb(rgb, DEFAULT_TERMINAL_THEME) for rgb in basic]
    standard_rgb = [color_to_rgb(rgb, DEFAULT_TERMINAL_THEME) for rgb in standard]
    bright_rgb = [color_to_rgb(rgb, DEFAULT_TERMINAL_THEME) for rgb in bright]

    theme = TerminalTheme(
        basic_rgb[0],
        basic_rgb[1],
        standard_rgb,
        bright_rgb,
    )

    return theme


def set_builtin_terminal_theme(theme_name: str) -> TerminalTheme:
    """Set the terminal theme.

    Optional, only needed if user wants ANSI colors to respect their
    terminal theme.

    Args:
        theme_name (str): Theme name. Must match one of the builtin
        `theme_name.theme` files.

    Returns:
        TerminalTheme: Terminal theme.
    """
    builtin_theme_paths = find_built_in_themes("terminal")

    selected_theme_path = [
        theme if theme.stem == theme_name else None for theme in builtin_theme_paths
    ]

    selected_theme = selected_theme_path[0]

    if not selected_theme:
        return DEFAULT_TERMINAL_THEME

    terminal_theme = terminal_theme_from_file(selected_theme)

    return terminal_theme


TERMINAL_THEME = set_builtin_terminal_theme("gruvbox")
