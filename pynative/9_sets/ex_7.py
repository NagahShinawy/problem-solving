"""
Exercise 7: Check if two sets have any elements in common. If yes, display the common elements.
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
"""


def is_empty(items):
    return True if items else False


set1 = {20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
print(set1 & set2)

print(is_empty(set1 & set2))