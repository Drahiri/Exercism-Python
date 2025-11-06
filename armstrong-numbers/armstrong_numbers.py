def is_armstrong_number(number: int) -> bool:
    """Checks if number is Armstrong number.

    :param number: int - number to test.
    :return: bool - true when number is Armstrong number.

    Armstrong number is a number that is the sum of its own digits each raised
    to the power of the number of digits.
    """

    str_num = str(number)
    return number == sum([int(x) ** len(str_num) for x in str_num])
