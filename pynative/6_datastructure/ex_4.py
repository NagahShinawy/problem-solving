"""
Original list  [11, 45, 8, 11, 23, 45, 23, 45, 89]
Printing count of each item   {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}
"""

from collections import Counter

counts = Counter([11, 45, 8, 11, 23, 45, 23, 45, 89])
counts = dict(counts)


print(counts)