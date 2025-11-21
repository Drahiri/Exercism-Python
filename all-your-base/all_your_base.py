def rebase(input_base, digits, output_base):
    if input_base < 2 or output_base < 2:
        raise ValueError(f"{'input' if input_base < 2 else 'output'} base must be >= 2")
