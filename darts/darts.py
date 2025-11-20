import math


def score(x: float, y: float) -> int:
    radius_to_points = {1: 10, 5: 5, 10: 1}  # {radius: points}
    distance = math.sqrt(x * x + y * y)
    scored = 0

    for radius, points in radius_to_points.items():
        if distance <= radius:
            scored = points
            break

    return scored
