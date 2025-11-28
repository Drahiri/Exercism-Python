NUMBERS = [
    "no",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
]


def recite(start: int, take: int = 1) -> list[str]:
    """Recite bottle song.

    :param start: int - from which number start the song.
    :param take: int - number of bottles to take
    :return: list[str] - bottle song.
    """

    result = []

    for taken in range(take):
        current = NUMBERS[start - taken]
        left = NUMBERS[start - taken - 1]
        last_bottle = current == NUMBERS[1]

        result.extend(
            [
                f"{current.title()} green {'bottles' if not last_bottle else 'bottle'} hanging on the wall,"
            ]
            * 2
        )
        result.append("And if one green bottle should accidentally fall,")
        result.append(
            f"There'll be {left} green {'bottle' if left == NUMBERS[1] else 'bottles'} hanging on the wall."
        )
        if taken + 1 != take:
            result.append("")

    return result
