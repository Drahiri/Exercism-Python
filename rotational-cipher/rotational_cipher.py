def rotate(text: str, key: int) -> str:
    encrypted = []
    for c in text:
        if c.isalpha():
            if c.islower():
                c = chr((ord(c) - 97 + key) % 26 + 97)
            else:
                c = chr((ord(c) - 65 + key) % 26 + 65)

        encrypted.append(c)

    return "".join(encrypted)
