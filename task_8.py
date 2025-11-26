def sort_string(s: str) -> str:
    """
    Sorts the characters in the input string in ascending order.

    This function takes a string, converts it into a list of characters,
    sorts the list in lexicographical order, and then joins the sorted
    characters back into a string.

    Args:
        s (str): The input string to be sorted.

    Returns:
        str: A new string containing the sorted characters of the input string.
    """
    chars = list(s)
    chars.sort()
    return ''.join(chars)


line = input()
print(sort_string(line))
