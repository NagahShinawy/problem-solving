"""
Exercise 6: Given the following two sets find the intersection and remove those elements from the first set
Expected Output:

First Set  {65, 42, 78, 83, 23, 57, 29}
Second Set  {67, 73, 43, 48, 83, 57, 29}

Intersection is  {57, 83, 29}
First Set after removing common element  {65, 42, 78, 23}
"""

first = {65, 42, 78, 83, 23, 57, 29}
second = {67, 73, 43, 48, 83, 57, 29}

in_first_but_no_in_second = first - second

print(in_first_but_no_in_second)

intersection = first & second
print(intersection)

# #############################

firstSet = {23, 42, 65, 57, 78, 83, 29}
secondSet = {57, 83, 29, 67, 73, 43, 48}

print("First Set ", firstSet)
print("Second Set ", secondSet)

intersection = firstSet.intersection(secondSet)
print("Intersection is ", intersection)
for item in intersection:
  firstSet.remove(item)

print("First Set after removing common element ", firstSet)