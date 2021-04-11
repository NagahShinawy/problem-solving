"""
Given a list of numbers, write a Python program to print all positive numbers in given list.

Example:

Input: list1 = [12, -7, 5, 64, -14]
Output: 12, 5, 64

Input: list2 = [12, 14, -95, 3]
Output: [12, 14, 3]
"""


def find_positive(numbers):
    return [num for num in numbers if num >= 0]


def find_positive2(numbers):
    return list(filter(lambda num: num >= 0, numbers))


print(find_positive([12, -7, 5, 64, -14]))
print(find_positive2([12, -7, 5, 64, -14]))