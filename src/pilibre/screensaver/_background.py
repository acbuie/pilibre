import random

from rich.text import Text

from pilibre._theme import theme


def _replace_single_char(text: Text, char: str, index: int) -> Text:
    """Replaces a single character in a `Text` object, at the index.

    Note that this will work with strings, too. In the context of this
    application, I will only be passing `Text`, to keep color or other
    `Rich` formatting.

    Args:
        text (Text): Text to replace within.
        char (str): Character to replace.
        index (int): Index at which to replace.

    Returns
        Text: Original text with the character replaced.
    """
    return text[:index] + char + text[index + 1 :]


def _check_if_empty_char(text: Text, index: int) -> bool:
    """Check if a character at the supplied index is a space character.

    Args:
        text (Text): Text to check within.
        index (int): Index at which to check for a space character.

    Returns
        bool: True, if the character is a space character.
    """
    text_as_string = text.plain
    char = text_as_string[index]
    return char.isspace()


def _replace_random_spaces(text: Text, char: str, num: int) -> Text:
    """Replace `num` random whitespaces in `text`, with `char`.

    Args:
        text (Text): Text to replace within.
        char (str): Character to replace with.
        num (int): Number of replacements to perform.

    Returns
        Text: Text
    """
    i = 0
    while i < num:
        index = random.randint(0, len(text) - 1)

        # If we randomly grab a non-whitespace character, try again
        if not _check_if_empty_char(text, index):
            continue

        text = _replace_single_char(text, char, index)
        i += 1

    return text


def construct_screensaver(foreground: Text, width: int) -> Text:
    """Constructs the starry background text for the screensaver.

    Args:
        foreground (Text): Foreground text.
        width (int): Maximum line width.

    Returns
        Text: Starry background, as Text.
    """
    new_line = Text("\n")
    lines = []

    for line in foreground.split():
        # line = Text(" " * width)
        line = _replace_random_spaces(line, "⋆", 10)
        line = _replace_random_spaces(line, "✷", 2)
        line = _replace_random_spaces(line, "∙", 4)
        line = _replace_random_spaces(line, "✦", 8)
        line = _replace_random_spaces(line, "✧", 2)

        line.set_length(width - 4)

        lines.append(line)

    background = new_line.join(lines)

    background.highlight_words("⋆", style=theme.styles["star.far"])
    background.highlight_words("✷", style=theme.styles["star.yellow"])
    background.highlight_words("∙", style=theme.styles["star.blue"])
    background.highlight_words("✦", style=theme.styles["star.near"])
    background.highlight_words("✧", style=theme.styles["star.hallow"])

    return background
