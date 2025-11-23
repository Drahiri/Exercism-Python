def encode(plain_text: str) -> str:
    plain_text = plain_text.lower()
    ciphered_text = []
    space_index = 0

    for c in plain_text:
        if c.isnumeric():
            ciphered_text.append(c)
        elif c.isalpha():
            ciphered_text.append(chr(219 - ord(c)))  # 219 = 97 + 122
        else:
            continue

        space_index += 1
        if space_index % 5 == 0:
            ciphered_text.append(" ")

    return "".join(ciphered_text).strip()


def decode(ciphered_text: str) -> str:
    # Remove spaces
    ciphered_text = "".join(ciphered_text.split())
    plain_letters = []
    for c in ciphered_text:
        if c.isnumeric():
            plain_letters.append(c)
        else:
            plain_letters.append(chr(219 - ord(c)))

    return "".join(plain_letters)
