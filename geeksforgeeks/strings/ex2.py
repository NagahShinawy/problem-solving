"""
We are given a string and we need to reverse words of a given string?

Examples:

Input : str = geeks quiz practice code
Output : str = code practice quiz geeks
"""


def reverse_words(text: str):
    return " ".join(text.split()[::-1])


print(reverse_words("geeks quiz practice code"))