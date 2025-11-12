def count_holes_letters(text: str) -> tuple[int, int]:
    """
    Count the number of letters with holes and without holes in the given text.

    Letters with holes are defined as: 'a', 'b', 'd', 'e', 'g', 'o', 'p', 'q'.
    This function counts both types of letters separately and returns the counts.

    Args:
        text (str): The input text to analyze.

    Returns:
        tuple[int, int]: A tuple containing two integers:
            - First element: count of letters with holes
            - Second element: count of letters without holes (but still alphabetic)
    """
    holes_letters = {'a', 'b', 'd', 'e', 'g', 'o', 'p', 'q'}
    holes_count = 0
    count = 0

    for char in text:
        match char:
            case c if c in holes_letters:
                holes_count += 1
            case c if c.isalpha():
                count += 1

    return holes_count, count


def get_words_holes(words: list[str]) -> list[str]:
    """
    Filter words that contain at least two letters with holes.

    Letters with holes are defined as: 'a', 'b', 'd', 'e', 'g', 'o', 'p', 'q'.
    This function returns a list of words from the input that have at least
    two such letters.

    Args:
        words (list[str]): List of words to filter.

    Returns:
        list[str]: List of words containing at least two letters with holes.
    """
    holes_letters = {'a', 'b', 'd', 'e', 'g', 'o', 'p', 'q'}
    result = []

    for word in words:
        hole_count = sum(1 for char in word if char in holes_letters)
        if hole_count >= 2:
            result.append(word)

    return result


def main() -> None:
    """Main function to execute the text analysis workflow."""
    text = input().lower()
    words = text.split()

    holes, no_holes = count_holes_letters(text)
    print(holes, no_holes)

    filtered_words = get_words_holes(words)
    print(filtered_words)


if __name__ == "__main__":
    main()