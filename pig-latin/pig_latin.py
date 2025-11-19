def translate(text: str) -> str:
    """Changes text into pil latin.

    :param text: str - text to translate.
    :return: str - translated text.

    Pig latin follows the following rules:
    * if word starts with a vowel, 'xr' or 'yt' - add 'ay' to the end.
    * if starts with consonant - move all consonants until first vowel to the end
     and add 'ay' to the end.
    * if starts with consonant followed by 'qu' - move preceeding consonants and 'qu'
     to end and add 'ay'.
    * if starts with constonant followed by 'y' - move preceeding consonants to the end
     and add 'ay' to the end.
    """
    vowels = ["a", "e", "i", "o", "u"]
    changed_words = []

    for word in text.split():
        if not (word[0] in vowels or word[:2] in ["xr", "yt"]):
            index = 0
            if word[0] == "y":
                index += 1
            while word[index] not in [*vowels, "y"]:
                index += 1
            if word[index - 1] + word[index] == "qu":
                index += 1

            word = word[index:] + word[:index]

        changed_words.append(word + "ay")

    return " ".join(changed_words)
