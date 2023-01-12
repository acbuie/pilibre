"""Module for a usage Meter."""

import random  # TODO: placeholder data

from rich.console import Console, ConsoleOptions, RenderResult
from rich.segment import Segment
from rich.style import Style

from pilibre._color import color_bar_colors
from pilibre.config.themes import TERMINAL_THEME


class Meter:
    """A usage meter."""

    def __init__(self, low_color: str, high_color: str) -> None:
        self.low = low_color
        self.high = high_color
        self._usage = 0

    def set_usage(self, usage: int) -> None:
        """Set usage percentage."""
        self._usage = usage

    @property
    def usage(self) -> int:
        """Get usage percentage."""
        return self._usage

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:

        width = options.max_width

        colors = color_bar_colors(self.low, self.high, width, TERMINAL_THEME)

        percentage = int(width * (self.usage / 100.0))
        chopped_colors = colors[0:percentage]

        for color in chopped_colors:
            yield Segment("\u2588", Style(color=color))


def generate_meter() -> Meter:
    """Wrapped for updating a `Meter` with `Rich.Live`."""
    meter = Meter("bright_white", "red")

    usage = random.randint(0, 100)  # TODO: placeholder data
    meter.set_usage(usage)

    return meter

    # with Live(generate_meter(), console=console, refresh_per_second=4) as live:
    #     for _ in range(20):
    #         time.sleep(0.5)
    #         live.update(generate_meter())
