"""
Python – Least Frequent Character in String
Output :
The original string is : GeeksforGeeks
The minimum of all characters in GeeksforGeeks is : f
"""

from collections import Counter


def least_frequent(text):
    chars = Counter(text)
    return sorted(chars, key=chars.get)


print(least_frequent("GeeksforGeeks"))
print(least_frequent("GeeksforGeeks")[0])

animals = [
    {'type': 'penguin', 'name': 'Stephanie', 'age': 8},
    {'type': 'elephant', 'name': 'Devon', 'age': 3},
    {'type': 'puma', 'name': 'Moe', 'age': 5}, ]


anm = sorted(animals, key=lambda animal: animal["age"])

print(anm)