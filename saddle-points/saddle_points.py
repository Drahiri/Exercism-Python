def saddle_points(matrix: list[list[int]]) -> list[dict[str, int]]:
    """Checks for possible location for tree house.

    :param matrix: list[list[int]] - matrix of hights of trees.
    :return: list[dict[str, int]] - list of possible row/column locations.
    """
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise ValueError("irregular matrix")

    highest_trees = list(map(max, matrix))
    lowest_trees = list(map(min, list(zip(*matrix))))

    return [
        {"row": i + 1, "column": j + 1}
        for i, h_tree in enumerate(highest_trees)
        for j, l_tree in enumerate(lowest_trees)
        if h_tree == l_tree
    ]
