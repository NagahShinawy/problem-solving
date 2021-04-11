"""
Given two numbers, write a Python code to find the Maximum of these two numbers.

Examples:

Input: a = 2, b = 4
Output: 4

Input: a = -1, b = -4
Output: -1
"""


def find_max(a, b):
    if a >= b:
        return a
    return b


print(find_max(3, 2))
print(find_max(3, 6))
print(find_max(3, 3))

print(max(7, 7))