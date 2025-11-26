def calculate_average() -> float:
    """
    Calculates arithmetic mean of input numbers.

    Args:
        None: Reads space-separated integers from standard input.

    Returns:
        float: Arithmetic mean of the input numbers.
    """
    numbers = list(map(int, input().split()))
    average = sum(numbers) / len(numbers)
    return average


print(calculate_average())
