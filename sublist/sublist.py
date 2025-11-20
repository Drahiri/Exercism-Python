EQUAL = 0
UNEQUAL = 1
SUBLIST = 2
SUPERLIST = 3


def check_contain_sublist(list_one: list, list_two: list) -> bool:
    len_one = len(list_one)
    len_two = len(list_two)
    return any(
        list_one[i : i + len_two] == list_two for i in range(len_one - len_two + 1)
    )


def sublist(list_one: list, list_two: list) -> int:
    value = UNEQUAL

    if list_one == list_two:
        value = EQUAL
    elif len(list_one) > len(list_two):
        if check_contain_sublist(list_one, list_two):
            value = SUPERLIST
    else:
        if check_contain_sublist(list_two, list_one):
            value = SUBLIST

    return value
