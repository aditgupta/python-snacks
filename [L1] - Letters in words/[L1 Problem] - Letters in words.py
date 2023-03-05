"""
Write a program that takes a string as input and prints the number of times each character appears in the string.
"""


def count_letters(word):
    letters = {}
    chars = list(word)
    for char in chars:
        letters[char] = letters.get(char, 0) + 1
    return letters


word = 'watermelon'
print(count_letters(word))