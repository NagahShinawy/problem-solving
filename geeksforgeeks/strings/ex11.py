"""
Given a string, count the number of vowels present in given string using Sets.

Prerequisite: Sets in Python

Examples:

Input : GeeksforGeeks
Output : No. of vowels : 5

Input : Hello World
Output : No. of vowels :  3
"""
VOWELS = "aeiou"


def count_vowels(text: str) -> int:
    counts = 0
    text = text.lower()
    for char in text:
        if char in VOWELS:
            counts += 1
    return counts


print(count_vowels("GeeksforGeeks"))
print(count_vowels("Hello World"))