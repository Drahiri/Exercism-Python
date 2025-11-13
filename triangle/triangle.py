def equilateral(sides: list[int | float]) -> bool:
    """Checks if triangle is equilateral (all sides same length).

    :param sides: list[int | float] - list of sides.
    :return: bool - is triangle equilateral?
    """
    return sides[0] == sides[1] and sides[0] == sides[2] if sides[0] > 0 else False


def isosceles(sides: list[int | float]) -> bool:
    """Checks if triangle is isosceles (two sides same length).

    :param sides: list[int | float] - list of sides.
    :return: bool - is triangle isosceles?
    """
    if any(side <= 0 for side in sides):
        return False

    if (
        sides[0] + sides[1] < sides[2]
        or sides[0] + sides[2] < sides[1]
        or sides[1] + sides[2] < sides[0]
    ):
        return False

    return sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]


def scalene(sides: list[int | float]) -> bool:
    return False
