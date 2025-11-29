COLORS = [
    "black",  # 0
    "brown",  # 0
    "red",  # 1
    "orange",  # 1
    "yellow",  # 1
    "green",  # 2
    "blue",  # 2
    "violet",  # 2
    "grey",  # 3
    "white",  # 3
]

METRIC = ["", "kilo", "mega", "giga"]


def label(colors: list[str]) -> str:
    """Changes bands colors into resistance text.

    :param colors: list[str] - color bands on resistor.
    :return: str - resistance with metric prefix.
    """
    first_band = COLORS.index(colors[0])
    second_band = COLORS.index(colors[1])
    third_band = COLORS.index(colors[2])

    value = (first_band * 10 + second_band) * 10**third_band
    metric = METRIC[(third_band + 1) // 3]

    return f"{f'{value} ' if value < 1000 else f'{value // (1000 ** METRIC.index(metric))} {metric}'}ohms"
