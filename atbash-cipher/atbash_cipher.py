def encode(plain_text):
    pass


def decode(ciphered_text: str) -> str:
    # Remove spaces
    ciphered_text = "".join(ciphered_text.split())
    plain_letters = []
    for c in ciphered_text:
        if c.isnumeric():
            plain_letters.append(c)
        else:
            plain_letters.append(chr(122 + (97 - ord(c))))

    return "".join(plain_letters)
