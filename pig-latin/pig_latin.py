def translate(text: str) -> str:
    vowels = ["a", "e", "i", "o", "u"]

    if text[0] in vowels or text[:2] in ["xr", "yt"]:
        text += "ay"

    return text
