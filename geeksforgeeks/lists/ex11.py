"""
Given a list in Python and a number x, count number of occurrences of x in the given list.

Examples:

Input : lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
         x = 10
Output : 3
10 appears three times in given list.

Input : lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
        x = 16
Output : 0
"""

from collections import Counter


def count_occurrences(items, query):
    if query not in items:
        return 0
    counts = 0
    for item in items:
        if item == query:
            counts += 1
    return counts


lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]

print(lst.count(10))
print(count_occurrences(lst, 10))
print(lst.count(1000))

cnts = Counter(lst)  # return dict like obj
print(cnts)
print(cnts[10])