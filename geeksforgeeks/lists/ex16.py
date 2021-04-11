"""
Given a list of numbers, the task is to write a Python program to find the largest number in given list.

Examples:

Input : list1 = [10, 20, 4]
Output : 20

Input : list2 = [20, 10, 20, 4, 100]
Output : 100
"""


def find_max(numbers):
    default_max = numbers[0]
    for num in numbers:
        if num > default_max:
            default_max = num
    return default_max


print(find_max([10, 30, 50, 34]))

numbs = [20, 10, 40, 30, 33]

numbs = sorted(numbs)

max_num = numbs[-1]
print(max_num)