"""
Exercise 5: Given a two list of equal size create a Python set such that it shows the element from both lists in the pair
Expected Output:

First List  [2, 3, 4, 5, 6, 7, 8]
Second List  [4, 9, 16, 25, 36, 49, 64]
Result is  {(6, 36), (8, 64), (4, 16), (5, 25), (3, 9), (7, 49), (2, 4)}
"""


def mixed_lists(list1: list, list2: list) -> set:
    if len(list1) != len(list2):
        return set()
    items = set()
    for index in range(len(list1)):
        items.add((list1[index], list2[index]))
    return items


itms1 = [2, 3, 4, 5, 6, 7, 8]
itms2 = [4, 9, 16, 25, 36, 49, 64]

print(mixed_lists(itms1, itms2))
# ###########################


firstList = [2, 3, 4, 5, 6, 7, 8]
print("First List ", firstList)

secondList = [4, 9, 16, 25, 36, 49, 64]
print("Second List ", secondList)

result = zip(firstList, secondList)
resultSet = set(result)
print(resultSet)