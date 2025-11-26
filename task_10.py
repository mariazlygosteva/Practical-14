def move_elements() -> None:
    """
    Moves reversed slice from first list to second list and prints both modified lists.

    Args:
        None: Reads all inputs from standard input.

    Returns:
        None: Results are printed to standard output.
    """
    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))
    start, end = map(int, input().split())

    elements_to_move = lst1[start - 1:end][::-1]
    lst2.extend(elements_to_move)
    lst1 = lst1[:start - 1] + lst1[end:]

    print(lst1)
    print(lst2)


move_elements()
