def is_triangle(sides: list[int | float]) -> bool:
    """Checks if sides can create triangle.

    :param sides: list[int | float] - list of triangle sides.
    :return: bool - can sides create triangle?
    """
    if any(side <= 0 for side in sides):
        return False

    if (
        sides[0] + sides[1] < sides[2]
        or sides[0] + sides[2] < sides[1]
        or sides[1] + sides[2] < sides[0]
    ):
        return False

    return True


def equilateral(sides: list[int | float]) -> bool:
    """Checks if triangle is equilateral (all sides same length).

    :param sides: list[int | float] - list of sides.
    :return: bool - is triangle equilateral?
    """
    return (
        sides[0] == sides[1] and sides[0] == sides[2] if is_triangle(sides) else False
    )


def isosceles(sides: list[int | float]) -> bool:
    """Checks if triangle is isosceles (two sides same length).

    :param sides: list[int | float] - list of sides.
    :return: bool - is triangle isosceles?
    """
    return (
        sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]
        if is_triangle(sides)
        else False
    )


def scalene(sides: list[int | float]) -> bool:
    """Checks if triangle is scalene (all sides different).

    :param sides: list[int | float] - list of sides.
    :return: bool - is triangle scalene?
    """
    return not (isosceles(sides) or equilateral(sides)) if is_triangle(sides) else False
