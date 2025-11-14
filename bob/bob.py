def response(hey_bob: str) -> str:
    """Bobs' response to statement.

    :param hey_bob: str - statement.
    :return: str - reply.

    Reply can be one of:
    - "Sure" - on statements ending with question mark (?).
    - "Whoa, chill out!" - on statements with all CAPITAL LETTERS.
    - "Calm down, I know what I'm doing!" - on statements with all
          CAPITAL LETTERS and question mark.
    - "Fine. Be that way!" - on empty or only whitespace statements.
    - "Whatever" - on any other statement.
    """
    statement = hey_bob.strip()
    response = ""

    if not statement:
        response = "Fine. Be that way!"
    elif statement.upper() == statement:
        if statement[-1] == "?":
            response = "Calm down, I know what I'm doing!"
        else:
            response = "Whoa, chill out!"
    elif statement[-1] == "?":
        response = "Sure."
    else:
        response = "Whatever."

    return response
