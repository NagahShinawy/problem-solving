"""
Exercise 10: Check if all items in the following tuple are the same
tuple1 = (45, 45, 45, 45)
Expected output:

True
"""


def all_the_same(items):
    if not items:
        return False
    itm = items[0]  # default
    for item in items:
        if item != itm:
            return False
    return True


def check(items):
    return all([item == items[0] for item in items])


print(all_the_same((45, 45, 45, 45)))
print(all_the_same((45, 34, 90)))
print(all_the_same((45, 45, 45, 46)))
print(all_the_same((44, 45, 45, 45)))
print(all_the_same([]))


print("#" * 30)

print(check([44, 44, 44]))
print(check([44, 44, 11]))
print(check([11, 44, 44]))