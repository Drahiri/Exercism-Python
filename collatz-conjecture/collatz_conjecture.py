def steps(number: int) -> int:
    """Calculated how many steps are required to reach 1.

    :param number: int - starting number.
    :return: int - number of steps.

    Function that returns number of steps that are required to reach 1 with
    following rules:
    * If number is even - divide it by 2.
    * If number is odd - multiply by 3 and add 1.
    """

    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    counter = 0
    while number != 1:
        number = number // 2 if number % 2 == 0 else 3 * number + 1
        counter += 1

    return counter
