"""Functions to create the PiLibre screensaver."""

import time

from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.text import Text

from pilibre.console import console
from pilibre.screensaver._background import construct_stars
from pilibre.screensaver._center import align_text
from pilibre.screensaver._clock import Clock


def create_screen(text: Text, console: Console) -> Layout:
    """Create a static screensaver.

    Args:
        text (Text): Text to display.
        console (Console): Console instance.

    Returns:
        Layout: Screensaver to display.
    """
    clock = Clock("America/Denver")  # TODO: pull automatically?

    aligned_text = align_text(text, console.width, console.height)
    stars = construct_stars(aligned_text, console.width)

    screen = Layout(
        Panel(
            stars,
            title=clock.date_title,
            title_align="left",
            border_style="black",
            height=console.height,
            width=console.width,
        )
    )

    return screen


def run_screensaver(seconds: int) -> None:
    """Run the screensaver, for the supplied amount of seconds.

    Args:
        seconds (int): Time to run screensaver, in seconds.

    Returns:
        None
    """
    clock = Clock("America/Denver")

    with Live(create_screen(clock.as_text(), console), refresh_per_second=4) as live:
        for _ in range(seconds):
            time.sleep(5)
            clock.update()
            live.update(create_screen(clock.as_text(), console))
