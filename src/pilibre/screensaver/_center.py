from rich.text import Text


def _center_horizontally(text: Text, width: int) -> Text:
    text_len = len(text.split()[0])  # Length of first line of text

    # Round down, -52 for text width and panel characters
    num_spaces = (width - text_len) // 2
    padding = Text((num_spaces * " "))

    lines = text.split()
    padded_lines: list[Text] = []

    for line in lines:
        centered_line = padding + line + padding
        centered_line.set_length((width - 2))

        padded_lines.append(centered_line)

    centered_text = Text("\n").join(padded_lines)

    return centered_text


def _center_vertically(text: Text, width: int, height: int) -> Text:
    blank_line = Text(" " * width + "\n")

    # Even number of lines, text is 6 lines tall
    if (height - 6) % 2 == 0:
        pad_num = (height - 6) // 2

        padding = blank_line.copy()
        if pad_num == 1:
            padding.append_text(text)
            return padding

        for _ in range(pad_num - 2):
            padding.append_text(blank_line)

        padding_bottom = padding.copy()
        padding.append_text(text)
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
            padding_top.append_text(text)
            return padding_top

        # Subtract 2: 1 because blank_line has \n, another for the panel
        for _ in range(top_num - 2):
            padding_top.append_text(blank_line)

        for _ in range(bottom_num - 2):
            padding_bottom.append_text(blank_line)

        padding_top.append_text(text)
        padding_top.append_text(padding_bottom)

        return padding_top


def align_text(text: Text, width: int, height: int) -> Text:
    """Manually construct the centered text.

    Note that this effectively does what `Rich.Align` does, but keeps
    the text as `Text`.

    Args:
        text (Text): ASCII text.
        width (int): Terminal width.
        height (int): Terminal height

    Returns:
        Text: Centered text.
    """
    horizontal = _center_horizontally(text, width)
    vertical = _center_vertically(horizontal, width, height)

    return vertical
