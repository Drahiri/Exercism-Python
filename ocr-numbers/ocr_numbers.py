NUMBERS = [
    [" _ ", "| |", "|_|", "   "],
    ["   ", "  |", "  |", "   "],
    [" _ ", " _|", "|_ ", "   "],
    [" _ ", " _|", " _|", "   "],
    ["   ", "|_|", "  |", "   "],
    [" _ ", "|_ ", " _|", "   "],
    [" _ ", "|_ ", "|_|", "   "],
    [" _ ", "  |", "  |", "   "],
    [" _ ", "|_|", "|_|", "   "],
    [" _ ", "|_|", " _|", "   "],
]


def convert(input_grid: list[str]) -> str:
    """Converts OCR numbers into string of numbers.

    :param input_grid: list - grid that creates OCR numbers.
    :return: str - converted OCR numbers to normal numbers.
    """
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")

    for row in range(4):
        if len(input_grid[row]) % 3 != 0:
            raise ValueError("Number of input columns is not a multiple of three")

    number_str = ""
    for row in range(0, len(input_grid), 4):
        for column in range(0, len(input_grid[0]), 3):
            number = []
            number.append(input_grid[row][column : column + 3])
            number.append(input_grid[row + 1][column : column + 3])
            number.append(input_grid[row + 2][column : column + 3])
            number.append(input_grid[row + 3][column : column + 3])

            try:
                number_str += str(NUMBERS.index(number))
            except ValueError:
                number_str += "?"
        number_str += ","

    return number_str[:-1]
