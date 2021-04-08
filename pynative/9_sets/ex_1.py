"""
Exercise 1: Add a list of elements to a given set
Given:

sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]
Expected output:

Note: Set is unordered.

{'Green', 'Yellow', 'Black', 'Orange', 'Red', 'Blue'}
"""


def add_list_to_set(set_items: set, list_items: list):
    # add for just add one item
    for item in list_items:
        set_items.add(item)
    return set_items


def update_set_with_list(set_items: set, list_items: list):
    # update: update with iter not just one item
    return set_items.update(list_items)


sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]
print(add_list_to_set(sampleSet, sampleList))