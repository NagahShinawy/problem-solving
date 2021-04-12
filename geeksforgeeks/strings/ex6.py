"""
Given a String, perform uppercase of later part of string.

Input : test_str = ‘geeksforgeek’
Output : geeksfORGEEK
Explanation : Latter half of string is uppercased.

Input : test_str = ‘apples’
Output : appLES
Explanation : Latter half of string is uppercased.
"""


def halfupper(word: str) -> str:
    mid = len(word) // 2 if len(word) % 2 == 0 else len(word) // 2 + 1
    return word[:mid] + word[mid:].upper()


print(halfupper("apples"))
print(halfupper("appxles"))
