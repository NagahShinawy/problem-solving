"""
Given a List. The task is to find the sum and average of the list. Average of the list is defined as the sum of the elements divided by the number of the elements.

Examples:

Input: [4, 5, 1, 2, 9, 7, 10, 8]
Output:
sum =  46
average =  5.75

Input: [15, 9, 55, 41, 35, 20, 62, 49]
Output:
sum =  286
average =  35.75
"""


def find_avg(items):
    return sum(items) / len(items)


print(find_avg([15, 9, 55, 41, 35, 20, 62, 49]))
print(sum([15, 9, 55, 41, 35, 20, 62, 49]))
