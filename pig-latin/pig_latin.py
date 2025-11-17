def translate(text: str) -> str:
    vowels = ["a", "e", "i", "o", "u"]

    # Rule 1
    if text[0] in vowels or text[:2] in ["xr", "yt"]:
        text += "ay"
    else:
        index = 0
        # Rule 4
        if text[0] == "y":
            index += 1
        # Rule 2
        while text[index] not in [*vowels, "y"]:
            index += 1
        # Rule 3
        if text[index - 1 : index + 1] == "qu":
            index += 1

        text = text[index:] + text[:index] + "ay"

    return text
