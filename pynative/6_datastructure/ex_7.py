"""
Exercise 7: Given two sets, Checks if One Set is a subset or superset of another Set. if the subset is found delete all elements from that set
Given:

firstSet = {27, 43, 34}
secondSet = {34, 93, 22, 27, 43, 53, 48}
Expected Output:

First Set  {57, 83, 29}
Second Set  {67, 73, 43, 48, 83, 57, 29}

First set is subset of second set - True
Second set is subset of First set -  False

First set is Super set of second set -  False
Second set is Super set of First set -  True

First Set  set()
Second Set  {67, 73, 43, 48, 83, 57, 29}
"""


def is_subset(set1, set2):
    return all(False for item in set1 if item not in set2)


items1 = {27, 43, 34}

itms2 = {34, 93, 22, 27, 43, 53, 48}

print(is_subset(items1, itms2))

print(itms2.issuperset(items1))


# ##########################

firstSet = {57, 83, 29}
secondSet = {57, 83, 29, 67, 73, 43, 48}

print("First Set ", firstSet)
print("Second Set ", secondSet)

print("First set is subset of second set -", firstSet.issubset(secondSet))
print("Second set is subset of First set - ", secondSet.issubset(firstSet))

print("First set is Super set of second set - ", firstSet.issuperset(secondSet))
print("Second set is Super set of First set - ", secondSet.issuperset(firstSet))

if firstSet.issubset(secondSet):
    firstSet.clear()

if secondSet.issubset(firstSet):
    secondSet.clear()

print("First Set ", firstSet)
print("Second Set ", secondSet)