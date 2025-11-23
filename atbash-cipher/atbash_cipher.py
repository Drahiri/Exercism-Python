import string


def change_letter(character: str) -> str:
    if character.isnumeric():
        return character
    elif character.isalpha():
        return chr(219 - ord(character))

    return ""


def encode(plain_text: str) -> str:
    plain_text = plain_text.lower()
    ciphered_text = []
    space_index = 0

    for c in plain_text:
        if c.isspace() or c in string.punctuation:
            continue

        ciphered_text.append(change_letter(c))

        space_index += 1
        if space_index % 5 == 0:
            ciphered_text.append(" ")

    return "".join(ciphered_text).strip()


def decode(ciphered_text: str) -> str:
    # Remove spaces
    ciphered_text = "".join(ciphered_text.split())
    plain_letters = []
    for c in ciphered_text:
        plain_letters.append(change_letter(c))

    return "".join(plain_letters)
