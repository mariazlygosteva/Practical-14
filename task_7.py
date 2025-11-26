def calculate_sums() -> tuple[int, int]:
    """
    Calculates sum of even and odd numbers from input list.

    Args:
        None: Reads space-separated integers from standard input.

    Returns:
        tuple[int, int]: Tuple containing (sum_of_evens, sum_of_odds).
    """
    numbers = list(map(int, input().split()))
    even_sum = sum(x for x in numbers if x % 2 == 0)
    odd_sum = sum(x for x in numbers if x % 2 != 0)
    return even_sum, odd_sum


even, odd = calculate_sums()
print(even, odd)
