def egg_count(display_value: int) -> int:
    """Shows actual egg count from displayed name.

    :param display_value: int - displayed value.
    :return: int - actual count of eggs.
    """
    counter = 0

    while display_value > 0:
        if display_value & 1:
            counter += 1
        display_value = display_value >> 1

    return counter
