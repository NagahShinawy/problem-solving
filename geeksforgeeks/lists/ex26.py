"""
Given start and end of a range, write a Python program to print all positive numbers in given range.

Example:

Input: start = -4, end = 5
Output: 0, 1, 2, 3, 4, 5

Input: start = -3, end = 4
Output: 0, 1, 2, 3, 4
"""


def find_pos_in_range(start, end):
    pos = [i for i in range(start, end + 1) if i >= 0]
    return pos


def find_pos_in_range2(start, end):
    pos = [num for num in filter(lambda num: num >= 0, range(start, end + 1))]
    return pos


print(find_pos_in_range(-4, 5))
print(find_pos_in_range2(-4, 5))
