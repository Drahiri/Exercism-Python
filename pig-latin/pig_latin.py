def translate(text: str) -> str:
    vowels = ["a", "e", "i", "o", "u"]

    # Rule 1
    if text[0] in vowels or text[:2] in ["xr", "yt"]:
        text += "ay"
    else:
        # Rule 2
        index = 0
        while text[index] not in vowels:
            index += 1

        text = text[index:] + text[:index] + "ay"

    return text
