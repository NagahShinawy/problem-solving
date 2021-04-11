"""
Given a list of numbers, write a Python program to print all even numbers in given list.

Example:

Input: list1 = [2, 7, 5, 64, 14]
Output: [2, 64, 14]

Input: list2 = [12, 14, 95, 3]
Output: [12, 14]
"""


def find_evens(numbers):
    # using list comp
    return [num for num in numbers if num % 2 == 0]


def find_evens2(numbers):
    # using filter
    return list(filter(lambda num: num % 2 == 0, numbers))


print(find_evens([2, 7, 5, 64, 14]))
print(find_evens2([2, 7, 5, 64, 14]))