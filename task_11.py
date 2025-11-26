def rotate_list() -> None:
    """
    Rotates a list left or right by specified number of steps.

    Args:
        None: Reads list and rotation command from standard input.

    Returns:
        None: Prints the rotated list to standard output.
    """
    lst = list(map(int, input().split()))
    command = input().strip()

    direction = command[0]
    steps = int(command[1:])

    match direction.upper():
        case 'R':
            steps = steps % len(lst)
            lst = lst[-steps:] + lst[:-steps]
        case 'L':
            steps = steps % len(lst)
            lst = lst[steps:] + lst[:steps]

    print(lst)


rotate_list()
