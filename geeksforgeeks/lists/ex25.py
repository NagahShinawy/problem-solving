"""
Given a list of numbers, write a Python program to print all negative numbers in given list.

Example:

Input: list1 = [12, -7, 5, 64, -14]
Output: -7, -14

Input: list2 = [12, 14, -95, 3]
Output: -95
"""


def find_neg(numbers):
    return [num for num in numbers if num < 0]


def find_neg2(numbers):
    return list(filter(lambda num: num < 0, numbers))


print(find_neg([12, -7, 5, 64, -14]))
print(find_neg2([12, -7, 5, 64, -14]))
