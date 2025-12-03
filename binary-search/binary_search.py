def find(search_list: list[int], value: int) -> int:
    """Checks index of a number in list.

    :param search_list: list - list of numbers.
    :param value: int - number to search in list.
    :return: int - index of value in array.

    If number does not exist in array raises `ValueError`.
    """
    index = 0
    while search_list:
        middle = len(search_list) // 2
        if search_list[middle] == value:
            index += middle
            return index
        elif search_list[middle] < value:
            index += middle + 1
            search_list = search_list[middle + 1 :]
        else:
            search_list = search_list[:middle]

    raise ValueError("value not in array")
