def is_isogram(string):
    # Sanitize string
    string = "".join(string.split())
    string = "".join(string.split("-"))
    string = string.lower()

    return len(set(string)) == len(string)

    # Alternative solution to match path where 'set' is still unknown.
    # Swap with previous return

    # letters = []
    # for c in string:
    #     if c in letters:
    #         return False
    #     else:
    #         letters.append(c)
    # return True
