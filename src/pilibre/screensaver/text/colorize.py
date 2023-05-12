"""Apply color styling to ASCII texts."""

from rich.text import Text

from pilibre._theme import theme

LINE_COLORS = [
    theme.styles["logo.lighter"],
    theme.styles["logo.light"],
    theme.styles["logo.neutral"],
    theme.styles["logo.dark"],
    theme.styles["logo.darker"],
    "",
]
SHADOW_COLOR = theme.styles["logo.shadow"]


def _paint_lines(text: list[str]) -> Text:
    """Apply a style to each line in the text.

    Args:
        text (list[str]): ASCII text.

    Returns:
        Text: Colored ASCII text.
    """
    ascii_text = Text()
    for i, line in enumerate(text):
        painted_line = Text.assemble((line, f"{LINE_COLORS[i]}"), "\n")
        ascii_text.append(painted_line)

    return ascii_text


def construct_text(text: list[str]) -> Text:
    """Colorize the ASCII text.

    This applies `_paint_lines`, which also colors the shadow
    characters. Calls `Text.highlight_regex` after to correctly color
    the shadow characters.

    Args:
        text (list[str]): ASCII text.

    Returns:
        Text: Finalized, colored ASCII text.
    """
    painted_text = _paint_lines(text)
    painted_text.highlight_regex(r"(?P<shadow>[╔╗╚╝═║])", style=SHADOW_COLOR)

    return painted_text
