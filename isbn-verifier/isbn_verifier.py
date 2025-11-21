def is_valid(isbn: str) -> bool:
    without_dashes = "".join(isbn.split("-"))

    if len(without_dashes) != 10:
        return False
    return True
