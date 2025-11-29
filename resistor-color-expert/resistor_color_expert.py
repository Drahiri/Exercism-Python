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

TOLERANCES = {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10,
}

METRIC = ["", "kilo", "mega", "giga"]


def resistor_label(colors: list[str]) -> str:
    """Translates band colors into resitance and tolerance.

    :param colors: list[str] - colors on resistor.
    :return: str - resitance and tolerance text.
    """

    colors_len = len(colors)
    if colors_len == 1:
        return "0 ohms"

    first_band = COLORS.index(colors[0])
    second_band = COLORS.index(colors[1])
    third_band = COLORS.index(colors[2])
    value = 0
    metric = ""
    tolerance = 0
    if colors_len == 4:
        value = (first_band * 10 + second_band) * 10**third_band
        metric = METRIC[(third_band + 1) // 3]
        tolerance = TOLERANCES[colors[3]]
    elif colors_len == 5:
        fourth_band = COLORS.index(colors[3])
        value = (first_band * 100 + second_band * 10 + third_band) * 10**fourth_band
        metric = METRIC[(fourth_band + 2) // 3]
        tolerance = TOLERANCES[colors[4]]

    if value >= 1000:
        metric_index = METRIC.index(metric)
        if value % (1000**metric_index) == 0:
            value //= 1000**metric_index
        else:
            value /= 1000**metric_index

    return f"{f'{value} {metric}'}ohms ±{tolerance}%"
