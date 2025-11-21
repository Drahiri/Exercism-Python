def rebase(input_base, digits, output_base):
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
