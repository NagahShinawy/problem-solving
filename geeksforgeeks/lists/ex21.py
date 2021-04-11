"""
Given starting and end points, write a Python program to print all odd numbers in that given range.

Example:

Input: start = 4, end = 15
Output: 5, 7, 9, 11, 13, 15

Input: start = 3, end = 11
Output: 3, 5, 7, 9, 11
"""


def find_odds_in_range(start, end):
    odds = [num for num in range(start, end + 1) if num % 2 != 0]
    return odds


def find_odds_in_range2(start, end):
    if start % 2 == 0:
        start += 1
    odds = [num for num in range(start, end + 1) if num % 2 != 0]
    return odds


print(find_odds_in_range(start=1, end=10))
print(find_odds_in_range(start=2, end=10))