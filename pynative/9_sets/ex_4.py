"""
Home » Python Exercises » Python Set Exercise with Solutions
Python Set Exercise with Solutions
Updated on: March 9, 2021 | Python Tags: Basics Python Python Exercises

TweetF  sharein  shareP  Pin
A set is an unordered collection of items. Every item is unique in it. i.e., the Python set doesn’t allow duplicates. This Python set exercise aims to help Python developers to learn and practice set operations. Here I am providing 10 set programs to enhance your coding skills. All questions are tested on Python 3.

Also Read:

Python Sets
Python Set Quiz
This Python set exercise includes the following: –

It contains 10 questions and solutions provided for each question.
This coding exercise is nothing but Python set assignments to solve, where you can solve different set programs and challenges.
This set exercise covers questions on Python set operations and manipulations, set functions.

When you complete each question, you get more familiar with the Python set. Let us know if you have any alternative solutions. It will help other developers.

Use Online Code Editor to solve exercise questions.

Read: Complete Guide on Python Sets.

Exercise 1: Add a list of elements to a given set
Given:

sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]
Expected output:

Note: Set is unordered.

{'Green', 'Yellow', 'Black', 'Orange', 'Red', 'Blue'}
Show Solution
sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]
sampleSet.update(sampleList)
print(sampleSet)
 Run Online
Exercise 2: Return a new set of identical items from a given two set

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
Expected output:

{40, 50, 30}
Show Solution
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.intersection(set2))
 Run Online
Exercise 3: Returns a new set with all items from both sets by removing duplicates
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
Expected output:

{70, 40, 10, 50, 20, 60, 30}
Note: set is unordered so not necessary this will be the order of the item.


Show Solution
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.union(set2))
 Run Online
Exercise 4: Given two Python sets, update the first set with items that exist only in the first set and not in the second set.
set1 = {10, 20, 30}
set2 = {20, 40, 50}
Expected output:

set1 {10, 30}
"""

set1 = {10, 20, 30}
set2 = {20, 40, 50}

result = set1 - set2

print(result)

# #######################

set1 = {10, 20, 30}
set2 = {20, 40, 50}

set1.difference_update(set2)
print(set1)

