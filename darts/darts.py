import math


def score(x: float, y: float) -> int:
    """Calculates earned points.

    :param x, y: float - coordinates where the dart landed.
    :return: int - earned points.

    Points are earned based on the distance from the center:
    * if distance is less than or equal 1 unit - 10 points
    * if distance is less than or equal 5 unit - 5 points
    * if distance is less than or equal 10 unit - 1 points
    * none of the above - 0 points
    """
    radius_to_points = {1: 10, 5: 5, 10: 1}  # {radius: points}
    distance = math.sqrt(x * x + y * y)
    scored = 0

    for radius, points in radius_to_points.items():
        if distance <= radius:
            scored = points
            break

    return scored
