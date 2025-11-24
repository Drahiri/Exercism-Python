def answer(question: str) -> int:
    # Remove 'What is' and '?'
    question = question.removeprefix("What is ").removesuffix("?")
    words = question.split()

    if len(words) == 1:
        return int(words[0])

    return 0
