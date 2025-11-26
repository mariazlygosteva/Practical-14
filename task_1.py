def process_numbers() -> list[int]:
    """
    Reads 10 integers and returns list of sums of previous and next elements.

    Args:
        None: Reads 10 integers from standard input.

    Returns:
        list[int]: List of 8 elements where each element is the sum of
                  numbers[i-1] + numbers[i+1] for indices 1 to 8.
    """
    numbers = [int(input()) for k in range(10)]
    new_list = [numbers[j - 1] + numbers[j + 1] for j in range(1, 9)]
    return new_list


print(process_numbers())
