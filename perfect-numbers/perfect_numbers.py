import math


def classify(number: int) -> str:
    """A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    divisors_sum = 0
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            divisors_sum += i
            if i != number // i:
                divisors_sum += number // i
    divisors_sum -= number

    classification = ""
    if divisors_sum == number:
        classification = "perfect"

    return classification
