"""
Given a list, write a Python program to swap first and last element of the list.

Examples:

Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]

Input : [1, 2, 3]
Output : [3, 2, 1]
"""


def swap_first_with_last(items: list):
    items[0], items[-1] = items[-1], items[0]
    return items


def swap_first_with_last2(items: list):
    start, *middle, end = items
    items = end, *middle, start
    return items


def swapList(list):
    first = list.pop(0)
    last = list.pop(-1)

    list.insert(0, last)
    list.append(first)

    return list


# Driver code
newList = [12, 35, 9, 56, 24]

print(swapList(newList))

print(swap_first_with_last([1, 2, 3]))
print(swap_first_with_last([12, 35, 9, 56, 24]))
print(swap_first_with_last2([12, 35, 9, 56, 24]))