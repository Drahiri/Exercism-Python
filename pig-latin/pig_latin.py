def translate(text: str) -> str:
    vowels = ["a", "e", "i", "o", "u"]
    text_list = text.split()
    changed_words = []

    for word in text_list:
        # Rule 1
        if word[0] in vowels or word[:2] in ["xr", "yt"]:
            changed_words.append(word + "ay")
        else:
            index = 0
            # Rule 4
            if word[0] == "y":
                index += 1
            # Rule 2
            while word[index] not in [*vowels, "y"]:
                index += 1
            # Rule 3
            if word[index - 1 : index + 1] == "qu":
                index += 1

            changed_words.append(word[index:] + word[:index] + "ay")

    return " ".join(changed_words)
