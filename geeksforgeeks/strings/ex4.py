"""
Python – Avoid Spaces in string length
Last Updated : 05 Sep, 2020
Given a String, compute all the characters, except spaces.

Input : test_str = ‘geeksforgeeks 33 best’
Output : 19
Explanation : Total characters are 19.

Input : test_str = ‘geeksforgeeks best’
Output : 17
Explanation : Total characters are 17 except spaces.
"""


def count_without_spaces(text: str) -> str:
    return len("".join([char for char in text if char != " "]))


def count_without_spaces2(text: str) -> str:
    return len("".join([char for char in filter(lambda char: char != " ", text)]))


print(count_without_spaces("geeksforgeeks 33 best"))
print(count_without_spaces2("geeksforgeeks 33 best"))
