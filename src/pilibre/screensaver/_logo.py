from rich.text import Text

from pilibre._theme import theme

# 50 characters, by 6 lines
LOGO_UNFORMATTED = [
    "██████╗ ██╗██╗     ██╗██████╗ ██████╗ ███████╗",
    "██╔══██╗╚═╝██║     ╚═╝██╔══██╗██╔══██╗██╔════╝",
    "██████╔╝██║██║     ██║██████╔╝██████╔╝█████╗  ",
    "██╔═══╝ ██║██║     ██║██╔══██╗██╔══██╗██╔══╝  ",
    "██║     ██║███████╗██║██████╔╝██║  ██║███████╗",
    "╚═╝     ╚═╝╚══════╝╚═╝╚═════╝ ╚═╝  ╚═╝╚══════╝",
]


LINE_COLORS = [
    theme.styles["logo.lighter"],
    theme.styles["logo.light"],
    theme.styles["logo.neutral"],
    theme.styles["logo.dark"],
    theme.styles["logo.darker"],
    "",
]
SHADOW_COLOR = theme.styles["logo.shadow"]


def _paint_lines(logo: list[str]) -> Text:
    """Apply a style to each line in the PiLibre logo.

    Args:
        logo (list[str]): PiLibre logo.

    Returns:
        Text: Colored logo.
    """
    text_logo = Text()
    for i, line in enumerate(logo):
        painted_line = Text.assemble((line, f"{LINE_COLORS[i]}"), "\n")
        text_logo.append(painted_line)

    return text_logo


def construct_logo(logo: list[str]) -> Text:
    """Colorize the PiLibre logo.

    This applies `_paint_lines`, which also colors the shadow
    characters. Calls `Text.highlight_regex` after to correctly color
    the shadow characters.

    Args:
        logo (list[str]): PiLibre logo.

    Returns:
        Text: Finalized, colored logo.
    """
    painted_logo = _paint_lines(logo)
    painted_logo.highlight_regex(r"(?P<shadow>[╔╗╚╝═║])", style=SHADOW_COLOR)

    return painted_logo


LOGO = construct_logo(LOGO_UNFORMATTED)
