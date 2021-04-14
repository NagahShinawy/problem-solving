"""
Python – Odd Frequency Characters

Sometimes, while working with Python strings,
we can have a problem in which we need to extract all the string characters which have odd number of occurrences.
This problem can have applications in domains such as data domain and day-day programming.
Let’s discuss certain ways in which this task can be performed.

Input : test_str = ‘geekforgeeks’
Output : [‘r’, ‘o’, ‘f’, ‘s’]

Input : test_str = ‘g’
Output : [‘g’]
"""

from collections import Counter


def odd_frequency(text):
    counts = {char: count for char, count in Counter(text).items() if count % 2 != 0}
    return counts


print(odd_frequency("geekforgeeks"))
print(odd_frequency("g"))