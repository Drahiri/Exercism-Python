def is_pangram(sentence: str) -> bool:
    """Checks if sentence if pangram.

    :param sentence: str - sentence to check.
    :return: bool - is sentence pangram?
    """
    # Sanitize sentence
    sentence = "".join(sentence.split())
    sentence = "".join(sentence.split("-"))
    sentence = "".join(sentence.split("_"))
    sentence = sentence.lower()

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    found = []

    for c in sentence:
        if c not in found and c in alphabet:
            found.append(c)

    return len(found) == 26
