def answer(question: str) -> int | float:
    # Remove 'What is', 'by' and '?'
    question = question.removeprefix("What is")
    question = question.removesuffix("?")
    question = question.replace("by", "")
    words = question.split()

    if not words:
        raise ValueError("syntax error")

    while len(words) > 1:
        try:
            number1 = int(words[0])
            number2 = int(words[2])
            operator = words[1]
            remaining = words[3:]

            match operator:
                case "plus":
                    number1 += number2
                case "minus":
                    number1 -= number2
                case "multiplied":
                    number1 *= number2
                case "divided":
                    number1 /= number2

            words = [number1, *remaining]
        except Exception:
            raise ValueError("syntax error")

    return int(words[0])
