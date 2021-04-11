"""
Given two numbers, write a Python code to find the Minimum of these two numbers.

Examples:

Input: a = 2, b = 4
Output: 2

Input: a = -1, b = -4
Output: -4
"""


def find_min(a, b):
    if a <= b:
        return a
    return b


print(find_min(3, 2))
print(find_min(3, 6))
print(find_min(3, 3))
print(min(7, 10))