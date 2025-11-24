def answer(question: str) -> int | float:
    # Remove 'What is', 'by' and '?'
    question = question.removeprefix("What is ")
    question = question.removesuffix("?")
    question = question.replace("by", "")
    words = question.split()

    if len(words) == 1:
        return int(words[0])

    result = 0
    while len(words) > 1:
        number1 = int(words[0])
        number2 = int(words[2])
        operator = words[1]
        remaining = words[3:]

        result = number1
        match operator:
            case "plus":
                result += number2
            case "minus":
                result -= number2
            case "multiplied":
                result *= number2
            case "divided":
                result /= number2

        words = [result, *remaining]

    return result
