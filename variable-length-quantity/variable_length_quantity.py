def encode(numbers: list[int]) -> list[int]:
    """Encodes numbers into variable length quantity.

    :param numbers: list[int] - list of numbers to encode.
    :return: list[int] - encoded numbers.
    """
    payload = []

    for number in numbers:
        buffer = number & 0x7F
        number = number >> 7
        while number > 0:
            buffer = buffer << 8
            buffer |= 0x80
            buffer += number & 0x7F
            number = number >> 7

        while True:
            payload.append(buffer & 0xFF)
            if buffer & 0x80:
                buffer = buffer >> 8
            else:
                break

    return payload


def decode(bytes_: list[int]) -> list[int]:
    """Decoded variable length quantity into number.

    :param bytes_: list[int] - list of bytes.
    :return: list[int] - list of decoded numbers.
    """
    numbers = []
    number = 0
    used_bytes = 0  # Used to check if number is correctly encoded in bytes

    for byte in bytes_:
        number = (number << 7) + (byte & 0x7F)
        used_bytes += 1
        if not (byte & 0x80):
            numbers.append(number)
            number = 0
            used_bytes = 0

    if used_bytes != 0:
        raise ValueError("incomplete sequence")

    return numbers
