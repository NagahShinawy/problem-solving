"""
Given a list of numbers, the task is to write a Python program to find the second largest number in given list.
Examples:

Input: list1 = [10, 20, 4]
Output: 10

Input: list2 = [70, 11, 20, 4, 100]
Output: 70
"""


def find_second_max(numbers):
    numbs = sorted(numbers)
    return numbs[-2]


def find_second_max2(numbers):
    numbs = sorted(numbers, reverse=True)
    return numbs[1]


print(find_second_max([10, 20, 4]))
print(find_second_max2([10, 20, 4]))