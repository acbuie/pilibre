"""Module for usage history graph."""

from collections import deque
from itertools import islice

from rich.console import Console, ConsoleOptions, RenderResult
from rich.style import Style
from rich.text import Text

from pilibre._color import color_bar_colors
from pilibre.config.themes import TERMINAL_THEME

GraphDict = dict[float, tuple[Text, Text]]


def _make_graph(low_color: str, high_color: str) -> GraphDict:
    """Construct the graph dictionary.

    Args:
        low_color (str): Low value color.
        high_color (str): High value color.

    Returns:
        GraphDict: Graph character dictionary.
    """
    colors = color_bar_colors(low_color, high_color, 16, TERMINAL_THEME)

    empty = Text("  ")

    graph = {
        0.0000: (
            empty,  # Top
            empty,  # Bottom
        ),
        0.0625: (
            empty,
            Text(" ▁", style=Style(color=colors[0])),
        ),
        0.1250: (
            empty,
            Text(" ▂", style=Style(color=colors[1])),
        ),
        0.1875: (
            empty,
            Text(" ▃", style=Style(color=colors[2])),
        ),
        0.2500: (
            empty,
            Text(" ▄", style=Style(color=colors[3])),
        ),
        0.3125: (
            empty,
            Text(" ▅", style=Style(color=colors[4])),
        ),
        0.3750: (
            empty,
            Text(" ▆", style=Style(color=colors[5])),
        ),
        0.4375: (
            empty,
            Text(" ▇", style=Style(color=colors[6])),
        ),
        0.5000: (
            empty,
            Text(" █", style=Style(color=colors[7])),
        ),
        0.5625: (
            Text(" ▁", style=Style(color=colors[8])),
            Text(" █", style=Style(color=colors[8])),
        ),
        0.6250: (
            Text(" ▂", style=Style(color=colors[9])),
            Text(" █", style=Style(color=colors[9])),
        ),
        0.6875: (
            Text(" ▃", style=Style(color=colors[10])),
            Text(" █", style=Style(color=colors[10])),
        ),
        0.7500: (
            Text(" ▄", style=Style(color=colors[11])),
            Text(" █", style=Style(color=colors[11])),
        ),
        0.8125: (
            Text(" ▅", style=Style(color=colors[12])),
            Text(" █", style=Style(color=colors[12])),
        ),
        0.8750: (
            Text(" ▆", style=Style(color=colors[13])),
            Text(" █", style=Style(color=colors[13])),
        ),
        0.9375: (
            Text(" ▇", style=Style(color=colors[14])),
            Text(" █", style=Style(color=colors[14])),
        ),
        1.0000: (
            Text(" █", style=Style(color=colors[15])),
            Text(" █", style=Style(color=colors[15])),
        ),
    }

    return graph


def _map_to_character(percentage: int, graph: GraphDict) -> tuple[Text, Text]:
    """Map a percentage value to a graph character.

    Args:
        percentage (int): Percentage. Between 0 and 100.

    Returns:
        tuple[Text, Text]: Graph characters.
    """
    unit_percentage = percentage / 100
    nearest_percentage = round(unit_percentage * 16) / 16

    return graph[nearest_percentage]


class Graph:
    """A usage history graph."""

    def __init__(self, low_color: str, high_color: str, size: int = 100) -> None:
        """Initialize the graph.

        Args:
            low_color (str): Color for low usage.
            high_color (str): Color for high usage.
            size (int, optional): Maximum size of the queue. Defaults to
            100.
        """
        self.graph_up = _make_graph(low_color, high_color)

        initial = [Text("  ") for _ in range(size)]
        self.queue_top = deque(initial, size)
        self.queue_bottom = deque(initial, size)

    def update_queue(self, value: int) -> None:
        """Add a value to the graph."""
        chars = _map_to_character(value, self.graph_up)

        self.queue_top.appendleft(chars[0])
        self.queue_bottom.appendleft(chars[1])

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:

        i = options.max_width

        display_top = list(islice(self.queue_top, i // 2))
        display_bottom = list(islice(self.queue_bottom, i // 2))

        graph_top = Text("").join(display_top)
        graph_bottom = Text("").join(display_bottom)

        graph = Text("\n").join([graph_top, graph_bottom])

        yield graph


# No 'wrapper' func needed, just call 'update_queue' on graph object
# graph = Graph("blue", "red")
# with Live(graph, console=console, refresh_per_second=4) as live:
#     for _ in range(50):
#         time.sleep(0.3)
#         graph.update_queue(random.randint(0, 100))
