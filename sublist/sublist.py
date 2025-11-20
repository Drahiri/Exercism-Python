EQUAL = 0
UNEQUAL = 1
SUBLIST = 2
SUPERLIST = 3


def sublist(list_one: list, list_two: list) -> int:
    value = UNEQUAL

    if list_one == list_two:
        value = EQUAL
    elif len(list_one) > len(list_two):
        for i in range(len(list_one) - len(list_two) + 1):
            if list_one[i : i + len(list_two)] == list_two:
                value = SUPERLIST
    elif len(list_one) < len(list_two):
        for i in range(len(list_two) - len(list_one) + 1):
            if list_two[i : i + len(list_one)] == list_one:
                value = SUBLIST

    return value
