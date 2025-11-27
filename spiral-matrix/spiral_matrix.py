def spiral_matrix(size: int) -> list[list[int]]:
    """Create matrix of 'size' where nubmers spirals inside.

    :param size: int - size of the matrix.
    :param: list[list[int]] - matrix of spiralling numbers.
    """

    spiral = [[0 for i in range(size)] for j in range(size)]

    dx, dy = (1, 0)
    x, y = (0, 0)

    for i in range(size * size):
        spiral[y][x] = i + 1

        if (
            any((x + dx >= size, y - dy >= size, y - dy < 0, x + dx < 0))
            or spiral[y - dy][x + dx]
        ):
            dx, dy = dy, -dx

        x += dx
        y -= dy

    return spiral
