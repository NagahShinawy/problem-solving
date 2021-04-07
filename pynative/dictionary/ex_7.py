

"""
Exercise 7: Check if a value 200 exists in a dictionary
sampleDict = {'a': 100, 'b': 200, 'c': 300}
Expected output:

True
"""


def is_exists(dic: dict, value):
    return True if value in dic.values() else False


sampleDict = {'a': 100, 'b': 200, 'c': 300}
print(is_exists(dic=sampleDict, value=2))
print(is_exists(dic=sampleDict, value=200))