"""
Given a list of numbers, the task is to write a Python program to find the smallest number in given list.
Examples:

Input : list1 = [10, 20, 4]
Output : 4

Input : list2 = [20, 10, 20, 1, 100]
Output : 1
"""

numbers = [10, 20, 4]

print(min(numbers))


def find_min(numbs):
    default = numbs[0]
    for num in numbs:
        if num < default:
            default = num
    return default


print(find_min(numbers))
numbers = sorted(numbers, reverse=True)
print(numbers[-1])
