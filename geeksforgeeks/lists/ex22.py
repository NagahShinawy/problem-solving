"""
Given a list of numbers, write a Python program to count Even and Odd numbers in a List.

Example:

Input: list1 = [2, 7, 5, 64, 14]
Output: Even = 3, odd = 2

Input: list2 = [12, 14, 95, 3]
Output: Even = 2, odd = 2
"""


def counts_evens_odds(numbers):
    evens = [num for num in numbers if num % 2 == 0]
    return {
        "evens": len(evens),
        "odds": len(numbers) - len(evens)
    }


print(counts_evens_odds([1, 2, 3, 4, 5, 6, 10, 12, 20, 40]))