from rich.align import Align
from rich.highlighter import RegexHighlighter
from rich.text import Text

LOGO_UNFORMATTED = [
    "██████╗ ██╗██╗     ██╗██████╗ ██████╗ ███████╗",
    "██╔══██╗  ║██║       ║██╔══██╗██╔══██╗██╔════╝",
    "██████╔╝██║██║     ██║██████╔╝██████╔╝█████╗  ",
    "██╔═══╝ ██║██║     ██║██╔══██╗██╔══██╗██╔══╝  ",
    "██║     ██║███████╗██║██████╔╝██║  ██║███████╗",
    "╚═╝     ╚═╝╚══════╝╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝",
]


LINE_COLORS = ["#ebdbb2", "#d3c5a0", "#bcaf8e", "#a4997c", "#8d836a", ""]
SHADOW_COLOR = "#3c3836"


def _paint_lines(logo: list[str]) -> Text:
    text_logo = Text()
    for i, line in enumerate(logo):
        painted_line = Text.assemble((line, f"{LINE_COLORS[i]}"), "\n")
        text_logo.append(painted_line)

    return text_logo


class _LogoHighlighter(RegexHighlighter):

    base_style = "logo."
    highlights = [r"(?P<shadow>[╔╗╚╝═║])"]


def construct_logo(logo: list[str]) -> Text:

    shadow_highlighter = _LogoHighlighter()

    # Color logo text, line by line. Highlight shadow characters
    painted_logo = _paint_lines(logo)
    highlighted_logo = shadow_highlighter(painted_logo)

    # Center logo in console, with padding
    aligned_logo = Align(highlighted_logo, align="center", vertical="middle")

    return aligned_logo


LOGO = construct_logo(LOGO_UNFORMATTED)
