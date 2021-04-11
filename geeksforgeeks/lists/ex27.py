"""
Given start and end of a range, write a Python program to print all negative numbers in given range.

Example:

Input: start = -4, end = 5
Output: -4, -3, -2, -1

Input: start = -3, end = 4
Output: -3, -2, -1
"""


def find_neg_in_range(start, end):
    neg = [i for i in range(start, end + 1) if i < 0]
    return neg


def find_neg_in_range2(start, end):
    neg = [num for num in filter(lambda num: num < 0, range(start, end + 1))]
    return neg


print(find_neg_in_range(-4, 5))
print(find_neg_in_range2(-4, 5))
