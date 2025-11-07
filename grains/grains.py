def square(number: int) -> int:
    """Calculates number of grains on chessboard square.

    :param number: int - square number in range 1-64.
    :return: int - number of grains.

    Function that calculates the number of grains on given square number.
    Number of grains is twice as much as on previous square.
    """
    if number <= 0 or number > 64:
        raise ValueError("Square must be between 1 and 64")

    return 1 << number - 1


def total() -> int:
    """Calculates sum of grains on whole chessboard.

    :return: int - sum of grains.
    """

    return (1 << 64) - 1
