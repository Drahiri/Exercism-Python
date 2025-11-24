def answer(question: str) -> int:
    # Remove 'What is' and '?'
    question = question.removeprefix("What is ").removesuffix("?")
    words = question.split()

    if len(words) == 1:
        return int(words[0])

    number1, operator, number2, *rest = words

    result = 0
    match operator:
        case "plus":
            result = int(number1) + int(number2)

    return result
