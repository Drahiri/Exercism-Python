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


def color_code(color: str) -> int:
    """Checks value of the color.

    :param color: str - name of the color.
    :return: int - value of the color.
    """
    return COLORS.index(color)


def colors() -> list[str]:
    """Lists resistor colors.

    :return: list[str] - list of color names.
    """
    return COLORS
