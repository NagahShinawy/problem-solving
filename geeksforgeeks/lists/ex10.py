"""
Python | Cloning or Copying a list

"""


def cloning(items: list):
    # using extend
    items_cp = []
    items_cp.extend(items)
    return items_cp


def cloning2(items: list):
    # using declaration
    items_cp = items
    return items_cp


def cloning3(items: list):
    # using list comp
    items_cp = [item for item in items]
    return items_cp


def cloning4(items: list):
    # using copy
    items_cp = items.copy()
    return items_cp


def cloning5(items: list):
    # using slicing
    items_cp = items[:]
    return items_cp


nmbs = [5, 6, 7]
print(cloning(nmbs))
print(cloning2(nmbs))
print(cloning3(nmbs))
print(cloning4(nmbs))
print(cloning5(nmbs))