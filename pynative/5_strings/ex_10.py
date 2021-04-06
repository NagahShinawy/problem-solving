from collections import Counter
"""
Exercise 10: Given an input string, count occurrences of all characters within a string
Given:

str1 = "ApPle"
Expected Outcome:

{'A': 1, 'p': 2, 'l': 1, 'e': 1}
"""


def count_occurrences(text: str) -> dict:
    counts = {}
    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    return counts


def count_occurrences2(text: str, insensitive=False) -> dict:
    counts = {}
    if insensitive:
        text = text.lower()

    for char in text:
        if char not in counts:
            counts[char] = text.count(char)

    return counts


print(count_occurrences("Apple"))
print(count_occurrences2("Applea", insensitive=True))

chars_by_count = Counter("Apple")
print({char: count for char, count in chars_by_count.items()})