from rich.color import Color
from rich.terminal_theme import TerminalTheme


def color_to_rgb(color: str, theme: TerminalTheme) -> tuple[int, int, int]:
    """Convert a color to its RGB triplet.

    Args:
        color (str): Color string. Passed to `Rich.Color.parse()`.
        theme (TerminalTheme): Terminal theme.

    Returns:
        tuple[int, int, int]: RGB triplet, as a tuple.
    """
    rich_color = Color.parse(color)
    true_color = rich_color.get_truecolor(theme=theme)

    r = true_color.red
    g = true_color.green
    b = true_color.blue

    return (r, g, b)


def _rgb_to_hex(rgb: tuple[int, int, int]) -> str:
    hex_color = "#" + "".join(f"{i:02X}" for i in rgb)
    return hex_color


def _linear_gradient(
    start_rgb: tuple[int, int, int], end_rgb: tuple[int, int, int], n: int
) -> list[tuple[int, int, int]]:
    """Compute a linear gradient, containing n colors between 2 colors.

    From https://bsouthga.dev/posts/color-gradients-with-python.

    Args:
        start_rgb (tuple[int, int, int]): RGB start color.
        end_rgb (tuple[int, int, int]): RGB end color.
        n (int): Number of colors in gradient.

    Returns:
        list[tuple[int, int, int]]: List of interpolated colors.
    """
    interpolated_rgbs = [start_rgb]

    for t in range(1, n):
        r = int(start_rgb[0] + (float(t) / (n - 1)) * (end_rgb[0] - start_rgb[0]))
        g = int(start_rgb[1] + (float(t) / (n - 1)) * (end_rgb[1] - start_rgb[1]))
        b = int(start_rgb[2] + (float(t) / (n - 1)) * (end_rgb[2] - start_rgb[2]))

        interpolated_rgbs.append((r, g, b))

    return interpolated_rgbs


def color_bar_colors(
    start_color: str, end_color: str, width: int, theme: TerminalTheme
) -> list[str]:
    """Create a color gradient (in hex) between two colors.

    The input color format is unspecified. Any string that can be parsed
    by `Rich.Color.parse` is valid.

    Args:
        start_color (str): Color gradient starting color.
        end_color (str): Color gradient ending color.
        width (int): Width of the gradient (effectively the terminal
        width)
        theme (TerminalTheme): Terminal theme.

    Returns:
        list[str]: Color gradient, in hex format.
    """
    rgb_start = color_to_rgb(start_color, theme=theme)
    rgb_end = color_to_rgb(end_color, theme=theme)

    rgb_gradient = _linear_gradient(rgb_start, rgb_end, width)

    hex_gradient = [_rgb_to_hex(color) for color in rgb_gradient]

    return hex_gradient
