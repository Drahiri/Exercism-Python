def is_isogram(string):
    # Sanitize string
    string = "".join(string.split())
    string = "".join(string.split("-"))
    string = string.lower()

    return len(set(string)) == len(string)
