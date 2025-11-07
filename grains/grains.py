def square(number: int) -> int:
    if number <= 0 or number > 64:
        raise ValueError("Square must be between 1 and 64")

    return 1 << number - 1


def total() -> int:
    pass
