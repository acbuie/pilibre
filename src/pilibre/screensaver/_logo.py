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


def construct_logo(logo: str = LOGO_UNFORMATTED) -> Text:

    shadow_highlighter = _LogoHighlighter()
    painted_logo = _paint_lines(logo)
    highlighted_logo = shadow_highlighter(painted_logo)

    return highlighted_logo


LOGO = construct_logo(LOGO_UNFORMATTED)
