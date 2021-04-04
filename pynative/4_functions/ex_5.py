"""
Exercise 5: Create an inner function to calculate the addition in the following way
Create an outer function that will accept two parameters, a and b
Create an inner function inside an outer function that will calculate the addition of a and b
At last, an outer function will add 5 into addition and return it
"""


def outer(a, b):
    def inner(x, y):
        return x + y

    return inner(a, b) + 5


print(outer(8, 7))
