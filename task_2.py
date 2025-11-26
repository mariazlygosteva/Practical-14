def process_numbers() -> list[int]:
    """
    Removes first occurrence of number 3 from input list.

    Args:
        None: Reads space-separated integers from standard input.

    Returns:
        list[int]: Modified list with first occurrence of 3 removed.
    """
    numbers = list(map(int, input().split()))
    numbers.remove(3)
    return numbers


print(process_numbers())
