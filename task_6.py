def find_divisors() -> list[int]:
    """
    Returns list of all divisors of input number in ascending order.

    Args:
        None: Reads an integer from standard input.

    Returns:
        list[int]: All divisors of the input number in ascending order.
    """
    num = int(input())
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors


print(find_divisors())
