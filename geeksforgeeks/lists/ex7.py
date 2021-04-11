"""
Check if element exists in list in Python

"""


def find_item(items, query):
    for item in items:
        if item == query:
            return True
    return False


print(find_item([3, 4, 7], 4))
print(find_item([3, 4, 7], 9))

print(4 in [9, 4, 5, 6])
print(4 in [9, 5, 6, 10])