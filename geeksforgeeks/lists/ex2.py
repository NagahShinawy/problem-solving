"""
Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list.

Examples:

Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
Output : [19, 65, 23, 90]

Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
Output : [1, 5, 3, 4, 2]
"""


def swap_positions(items, pos1, pos2):
    index1 = pos1 - 1
    index2 = pos2 - 1
    items[index1], items[index2] = items[index2], items[index1]
    return items


List = [23, 65, 19, 90]
print(swap_positions(List, pos1=1, pos2=3) == [19, 65, 23, 90])
print(swap_positions([1, 2, 3, 4, 5], pos1=2, pos2=5) == [1, 5, 3, 4, 2])


# Swap function
def swapPositions(list, pos1, pos2):
    # Storing the two elements
    # as a pair in a tuple variable get
    get = list[pos1], list[pos2]

    # unpacking those elements
    list[pos2], list[pos1] = get

    return list


# Driver Code
List = [23, 65, 19, 90]

pos1, pos2 = 1, 3
print(swapPositions(List, pos1 - 1, pos2 - 1))