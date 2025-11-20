EQUAL = 0
UNEQUAL = 1
SUBLIST = 2
SUPERLIST = 3


def sublist(list_one: list, list_two: list) -> int:
    if list_one == list_two:
        return EQUAL

    elif len(list_one) > len(list_two):
        for i in range(len(list_one) - len(list_two) + 1):
            if list_one[i : i + len(list_two)] == list_two:
                return SUPERLIST

    elif len(list_one) < len(list_two):
        for i in range(len(list_two) - len(list_one) + 1):
            if list_two[i : i + len(list_one)] == list_one:
                return SUBLIST

    return UNEQUAL
