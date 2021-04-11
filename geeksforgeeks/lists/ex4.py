"""
Python | Ways to find length of list

"""
from operator import length_hint


def length(items):
    counter = 0
    for _ in items:
        counter += 1
    return counter


print(length("test"))
print(len("test"))
print(length_hint("test"))