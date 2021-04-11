"""
Given a list of numbers, write a Python program to count positive and negative numbers in a List.

Example:

Input: list1 = [2, -7, 5, -64, -14]
Output: pos = 2, neg = 3

Input: list2 = [-12, 14, 95, 3]
Output: pos = 3, neg = 1
"""


def count_neg_post(numbers):
    posv = [num for num in numbers if num >= 0]
    return {
        "posv": len(posv),
        "neg": len(numbers) - len(posv)
    }


print(count_neg_post([2, -7, 5, -64, -14]))