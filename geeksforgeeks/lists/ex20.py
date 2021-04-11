"""
Given starting and end points, write a Python program to print all even numbers in that given range.

Example:

Input: start = 4, end = 15
Output: 4, 6, 8, 10, 12, 14

Input: start = 8, end = 11
Output: 8, 10
"""


def find_evens_in_range(start, end):
    evens = []
    for i in range(start, end + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens


def find_evens_in_range2(start, end):
    evens = [num for num in range(start, end + 1) if num % 2 == 0]
    return evens


def find_evens_in_range3(start, end):
    if start % 2 != 0:
        start += 1
    evens = [num for num in range(start, end + 1, 2)]
    return evens


print(find_evens_in_range(1, 10))
print(find_evens_in_range2(1, 10))
print(find_evens_in_range3(1, 10))
print(find_evens_in_range3(2, 10))