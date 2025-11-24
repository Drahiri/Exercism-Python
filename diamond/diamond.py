def rows(letter: str) -> list[str]:
    """Creates letters diamond shape.

    :param letter: str - letter to which diamond should be created.
    :return: list - list of lines creating diamond.
    """

    half_size = ord(letter) - 64
    diamond = []

    for i in range(half_size):
        line = [" "] * (half_size * 2 - 1)
        line[half_size - 1 - i] = chr(i + 65)
        line[half_size - 1 + i] = chr(i + 65)
        diamond.append("".join(line))

    bottom_part = diamond[:-1]
    bottom_part.reverse()
    diamond.extend(bottom_part)

    return diamond
