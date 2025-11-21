def rebase(input_base, digits, output_base):
    if input_base < 2 or output_base < 2:
        raise ValueError(f"{'input' if input_base < 2 else 'output'} base must be >= 2")

    for digit in digits:
        if digit < 0 or digit >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
