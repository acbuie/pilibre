"""Clock figures."""


NUMBERS = {
    "1": [
        " ██╗",
        "███║",
        "╚██║",
        " ██║",
        " ██║",
        " ╚═╝",
    ],
    "2": [
        "██████╗ ",
        "╚════██╗",
        " █████╔╝",
        "██╔═══╝ ",
        "███████╗",
        "╚══════╝",
    ],
    "3": [
        "██████╗ ",
        "╚════██╗",
        " █████╔╝",
        " ╚═══██╗",
        "██████╔╝",
        "╚═════╝ ",
    ],
    "4": [
        "██╗  ██╗",
        "██║  ██║",
        "███████║",
        "╚════██║",
        "     ██║",
        "     ╚═╝",
    ],
    "5": [
        "███████╗",
        "██╔════╝",
        "███████╗",
        "╚════██║",
        "███████║",
        "╚══════╝",
    ],
    "6": [
        " ██████╗ ",
        "██╔════╝ ",
        "███████╗ ",
        "██╔═══██╗",
        "╚██████╔╝",
        " ╚═════╝ ",
    ],
    "7": [
        "███████╗",
        "╚════██║",
        "    ██╔╝",
        "   ██╔╝ ",
        "   ██║  ",
        "   ╚═╝  ",
    ],
    "8": [
        " █████╗ ",
        "██╔══██╗",
        "╚█████╔╝",
        "██╔══██╗",
        "╚█████╔╝",
        " ╚════╝ ",
    ],
    "9": [
        " █████╗ ",
        "██╔══██╗",
        "╚██████║",
        " ╚═══██║",
        " █████╔╝",
        " ╚════╝ ",
    ],
    "0": [
        " ██████╗ ",
        "██╔═████╗",
        "██║██╔██║",
        "████╔╝██║",
        "╚██████╔╝",
        " ╚═════╝ ",
    ],
    ":": [
        "   ",
        "██╗",
        "╚═╝",
        "██╗",
        "╚═╝",
        "   ",
    ],
}

# TODO: Add AM and PM characters


def construct_time(characters: list[str]) -> list[str]:
    """Creates an ASCiI clock from an input of numbers.

    I am positve there is a more elegant way to do this.

    Returns:
        list[str]: ASCII clock strings.
    """
    ascii_nums = [NUMBERS[char] for char in characters]

    buffer = "  "

    # Lines one through 6 of the clock, zero indexed to match below
    line_0 = []
    line_1 = []
    line_2 = []
    line_3 = []
    line_4 = []
    line_5 = []

    for num in ascii_nums:
        line_0.append(num[0])
        line_1.append(num[1])
        line_2.append(num[2])
        line_3.append(num[3])
        line_4.append(num[4])
        line_5.append(num[5])

    clock_0 = f"{buffer}".join(line_0)
    clock_1 = f"{buffer}".join(line_1)
    clock_2 = f"{buffer}".join(line_2)
    clock_3 = f"{buffer}".join(line_3)
    clock_4 = f"{buffer}".join(line_4)
    clock_5 = f"{buffer}".join(line_5)

    clock = [
        clock_0,
        clock_1,
        clock_2,
        clock_3,
        clock_4,
        clock_5,
    ]

    return clock
