"""
Given a string. The task is to print all words with even length in the given string.

Examples:

Input: s = "This is a python abc language tes"
Output: This
        is
        python
        language

Input: s = "i am muskan"
Output: am
        muskan

"""


def is_even_len(word):
    return True if len(word) % 2 == 0 else False


def word_even_len(wrds):
    return [word for word in wrds if is_even_len(word)]


text = "This is a python abc language tes"

words = [word for word in text.split()]


print(word_even_len(words))


