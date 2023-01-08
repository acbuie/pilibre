from rich.text import Text


def _center_horizontally(logo: Text, width: int) -> Text:
    # Round down, -52 for logo width and panel characters
    num_spaces = (width - 52) // 2
    padding = Text((num_spaces * " "))

    lines = logo.split()
    padded_lines: list[Text] = []

    for line in lines:
        centered_line = padding + line + padding
        centered_line.set_length((width - 2))

        padded_lines.append(centered_line)

    centered_logo = Text("\n").join(padded_lines)

    return centered_logo


def _center_vertically(logo: Text, width: int, height: int) -> Text:
    blank_line = Text(" " * width + "\n")

    # Even number of lines, logo is 6 lines tall
    if (height - 6) % 2 == 0:
        pad_num = (height - 6) // 2

        padding = blank_line.copy()
        if pad_num == 1:
            padding.append_text(logo)
            return padding

        for _ in range(pad_num - 2):
            padding.append_text(blank_line)

        padding_bottom = padding.copy()
        padding.append_text(logo)
        padding.append_text(padding_bottom)

        return padding

    # Odd number of lines
    else:
        pad_num = height - 6

        top_num = ((pad_num - 1) // 2) + 1
        bottom_num = (pad_num - 1) // 2

        padding_top = blank_line.copy()
        padding_bottom = blank_line.copy()

        if pad_num == 1:
            padding_top.append_text(logo)
            return padding_top

        # Subtract 2: 1 because blank_line has \n, another for the panel
        for _ in range(top_num - 2):
            padding_top.append_text(blank_line)

        for _ in range(bottom_num - 2):
            padding_bottom.append_text(blank_line)

        padding_top.append_text(logo)
        padding_top.append_text(padding_bottom)

        return padding_top


def align_logo(logo: Text, width: int, height: int) -> Text:
    """Manually construct the centered logo.

    Note that this effectively does what `Rich.Align` does, but keeps
    the logo as `Text`.

    Args:
        logo (Text): Logo text.
        width (int): Terminal width.
        height (int): Terminal height

    Returns:
        Text: Centered logo.
    """
    horizontal = _center_horizontally(logo, width)
    vertical = _center_vertically(horizontal, width, height)

    return vertical
