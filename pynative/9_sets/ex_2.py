"""
Exercise 2: Return a new set of identical items from a given two set

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
Expected output:

{40, 50, 30}
"""

numbers1 = {10, 20, 30, 40, 50}
numbers2 = {30, 40, 50, 60, 70}

intersection = numbers1 & numbers2

print(intersection)

print(numbers1.intersection(numbers2))