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


def decode(bytes_):
    pass
