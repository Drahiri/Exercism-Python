def rebase(input_base: int, digits: list[int], output_base: int) -> list[int]:
    """Changes number from one base to another base.

    :param input_base: int - base in which `digits` are.
    :param digits: list[int] - digits in `input_base` to rebase.
    :param output_base: int - base to which rebase `digits`.
    :return: list[int] - digits that make rebased number.
    """
    if input_base < 2 or output_base < 2:
        raise ValueError(f"{'input' if input_base < 2 else 'output'} base must be >= 2")

    power = len(digits) - 1
    in_decimal = 0
    for i, digit in enumerate(digits):
        if digit < 0 or digit >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")

        in_decimal += digit * input_base ** (power - i)

    if in_decimal == 0:
        return [0]

    in_output_base = []
    while in_decimal != 0:
        in_output_base.append(in_decimal % output_base)
        in_decimal //= output_base

    in_output_base.reverse()
    return in_output_base
