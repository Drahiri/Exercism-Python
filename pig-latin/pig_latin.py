def translate(text: str) -> str:
    vowels = ["a", "e", "i", "o", "u"]
    changed_words = []

    for word in text.split():
        if not (word[0] in vowels or word[:2] in ["xr", "yt"]):
            index = 0
            if word[0] == "y":
                index += 1
            while word[index] not in [*vowels, "y"]:
                index += 1
            if word[index - 1 : index + 1] == "qu":
                index += 1

            word = word[index:] + word[:index]

        changed_words.append(word + "ay")

    return " ".join(changed_words)
