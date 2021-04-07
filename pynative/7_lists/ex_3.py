"""
Exercise 3: Given a Python list of numbers. Turn every item of a list into its square
Given:

aList = [1, 2, 3, 4, 5, 6, 7]

Expected output:


[1, 4, 9, 16, 25, 36, 49]
"""
from typing import Union


def to_square(numbers: Union[list, tuple]):
    return [(num, num ** 2) for num in numbers]


print(to_square([1, 2, 3, 4, 5, 6, 7]))