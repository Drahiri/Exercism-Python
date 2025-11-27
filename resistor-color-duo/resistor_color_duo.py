COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]


def value(colors: list[str]) -> int:
    """Checks value of 2 resistors colors.

    :param colors: list[str] - list of colors on resistor.
    :return: int - value of 2 resistor colors.
    """
    return COLORS.index(colors[0]) * 10 + COLORS.index(colors[1])
