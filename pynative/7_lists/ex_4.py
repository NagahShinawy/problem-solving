"""
Exercise 4: Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
Expected output:

['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
"""


def concatenate(items1, items2):
    result = []
    for item in items1:
        for value in items2:
            result.append(item + value)

    return result


def concatenate2(items1, items2):
    return [x + y for x in items1 for y in items2]


list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
expected = ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
print(expected)
print(concatenate(list1, list2) == expected)
print(concatenate2(list1, list2) == expected)