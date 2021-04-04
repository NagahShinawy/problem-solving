"""
Exercise 6: Write a recursive function to calculate the sum of numbers from 0 to 10

Expected Output:

55
"""

total = 0


# Python program to find the sum of natural using recursive function


def calculate(start, end):
    if start >= end:
        return end
    else:
        return end + calculate(start, end - 1)


print(calculate(11, 10))
