import string


sentence = input()
words = sentence.split()
new_list = [word.strip(string.punctuation) for word in words]
print(new_list)