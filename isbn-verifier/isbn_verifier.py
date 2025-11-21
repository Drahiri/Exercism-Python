def is_valid(isbn: str) -> bool:
    without_dashes = "".join(isbn.split("-"))

    if len(without_dashes) != 10:
        return False

    result = 0
    ord_0 = ord("0")
    ord_9 = ord("9")
    for i, number in enumerate(without_dashes):
        if ord_0 <= ord(number) <= ord_9:
            result += int(number) * (10 - i)
        else:
            if number == "X" and i == len(without_dashes) - 1:
                result += 10
            else:
                return False

    return result % 11 == 0
