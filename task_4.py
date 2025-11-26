import string


def get_unique_words() -> list[str]:
    """
    Returns list of unique words from input string with punctuation removed.

    Args:
        None: Reads a string from standard input.

    Returns:
        list[str]: List of unique words without punctuation.
    """
    sentence = input()
    words = [word.strip(string.punctuation) for word in sentence.split()]
    unique_words = list(set(words))
    return unique_words


print(get_unique_words())
