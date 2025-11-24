def answer(question: str) -> int:
    # Remove 'What is', 'by' and '?'
    question = question.removeprefix("What is ")
    question = question.removesuffix("?")
    words = question.split()

    if len(words) == 1:
        return int(words[0])

    number1 = int(words[0])
    number2 = int(words[2])
    operator = words[1]
    words = words[3:]

    result = 0
    match operator:
        case "plus":
            result = number1 + number2
        case "minus":
            result = number1 - number2

    return result
