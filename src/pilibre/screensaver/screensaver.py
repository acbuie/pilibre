import time

from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.text import Text

from pilibre.console import console
from pilibre.screensaver._background import construct_screensaver
from pilibre.screensaver._center import align_logo
from pilibre.screensaver._clock import format_datetime_title
from pilibre.screensaver._logo import LOGO


def create_screen(logo: Text, console: Console) -> Layout:
    date_time = format_datetime_title("America/Denver")

    aligned_logo = align_logo(logo, console.width, console.height)
    stars = construct_screensaver(aligned_logo, console.width)

    screen = Layout(
        Panel(
            stars,
            title=date_time,
            title_align="left",
            border_style="black",
        )
    )

    return screen


def run_screensaver() -> None:
    with Live(create_screen(LOGO, console), refresh_per_second=4) as live:
        for _ in range(10):
            time.sleep(1)
            live.update(create_screen(LOGO, console))
