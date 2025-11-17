def is_paired(input_string: str) -> bool:
    """Checks if brackets, braces and parentheses are correctly matched and nested.

    :param input_string: str - string to check.
    :return: bool - are correctly matched and nested?
    """
    matching_bracket = {"[": "]", "{": "}", "(": ")"}
    found_brackets = []

    for c in input_string:
        if c in matching_bracket.keys():
            found_brackets.append(c)
        elif c in matching_bracket.values():
            if not found_brackets or c != matching_bracket[found_brackets.pop()]:
                return False

    return not found_brackets
