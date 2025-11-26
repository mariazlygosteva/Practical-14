import string


def process_sentence() -> list[str]:
    """
    Removes punctuation from start and end of each word in input sentence.

    Args:
        None: Reads a string from standard input.

    Returns:
        list[str]: List of words with punctuation stripped from ends.
    """
    sentence = input()
    words = sentence.split()
    new_list = [word.strip(string.punctuation) for word in words]
    return new_list


print(process_sentence())
