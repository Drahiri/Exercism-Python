def update_fields(garden: list[list], row: int, column: int) -> None:
    OFFSETS = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    garden[row][column] = "*"

    for x, y in OFFSETS:
        if garden[row + x][column + y] != "*":
            garden[row + x][column + y] = str(int(garden[row + x][column + y]) + 1)


def annotate(garden: list[str]) -> list[str]:
    """Counts how many flowers (*) are adjacent to one field.

    :param garden: list[str] - 2D list representing fields in garden with flowers.
    :return: list[str] - alternated garden with count of flowers.
    """
    if not garden:
        return []

    # Create new 2D table with padding
    filled_row = ["0"] * (len(garden[0]) + 2)
    count_garden = []
    for i in range(len(garden) + 2):
        count_garden.append(filled_row.copy())

    for i, line in enumerate(garden):
        if len(line) != len(garden[i - 1]):
            raise ValueError("The board is invalid with current input.")

        for j, field in enumerate(line):
            if field == "*":
                update_fields(count_garden, i + 1, j + 1)
            elif not field.isspace():
                raise ValueError("The board is invalid with current input.")

    return ["".join(line[1:-1]).replace("0", " ") for line in count_garden[1:-1]]
