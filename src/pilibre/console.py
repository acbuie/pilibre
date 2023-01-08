"""Provides the `console` to all submodules.

Attributes:
    console (Console): Global console varaible.
"""

from rich.console import Console

from pilibre._theme import theme

console = Console(theme=theme)
