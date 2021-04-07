"""
Exercise 5: Given a two Python list. Iterate both lists simultaneously such that list1 should display item in original order and list2 in reverse order
Given

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

Expected output:

10 400
20 300
30 200
40 100
"""


def show_items(items1, items2):
    for x, y in zip(items1, items2[::-1]):
        print(x, y)


list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

show_items(list1, list2)