def steps(number: int) -> int:
    counter = 0
    while number != 1:
        number = number // 2 if number % 2 == 0 else 3 * number + 1
        counter += 1

    return counter
