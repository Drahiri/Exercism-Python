def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    """Find all anagrams from candidates.

    :param word: str - base word for anagram.
    :param candidates: list - possible anagrams of the word.
    :return: list - list of anagrams from candidates.
    """
    result = []
    word = word.lower()

    for candidate in candidates:
        lower_candidate = candidate.lower()
        if len(lower_candidate) != len(word) or word == lower_candidate:
            continue

        word_list = sorted(list(word))
        candidate_list = sorted(list(lower_candidate))

        if word_list == candidate_list:
            result.append(candidate)

    return result
