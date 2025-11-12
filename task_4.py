import string


sentence = input()
words = [word.strip(string.punctuation) for word in sentence.split()]
unique_words = list(set(words))
print(unique_words)
