"""
Exercise 3: Returns a new set with all items from both sets by removing duplicates
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
Expected output:

{70, 40, 10, 50, 20, 60, 30}
"""

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

union = set1.union(set2)
print(union)

# ##############################################

# Program to perform different set operations
# as we do in  mathematics

# sets are define
A = {0, 2, 4, 6, 8}
B = {1, 2, 3, 4, 5}

# union
print("Union :", A | B)

# intersection
print("Intersection :", A & B)

# difference
print("Difference :", A - B)

# symmetric difference
print("Symmetric difference :", A ^ B)