import string


def process_text() -> None:
    """
    Processes multi-line text to count word frequency and output in descending order.

    Args:
        None: Reads multi-line text from standard input until empty line.

    Returns:
        None: Prints words in descending order of frequency.
    """
    text_lines = []

    while True:
        line = input()
        if line == '':
            break
        text_lines.append(line)

    full_text = ' '.join(text_lines).lower()
    translator = str.maketrans('', '', string.punctuation)
    clean_text = full_text.translate(translator)
    words = clean_text.split()

    word_count = {}
    order = []

    for word in words:
        if word not in word_count:
            word_count[word] = 0
            order.append(word)
        word_count[word] += 1

    word_freq = []
    a = word_freq

    for word in order:
        word_freq.append((word_count[word], word))

    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i][0] < a[j][0]:
                a[i], a[j] = a[j], a[i]

    sorted_words = [pair[1] for pair in a]

    for word in sorted_words:
        print(word)


process_text()
