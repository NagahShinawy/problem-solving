"""
Given the string, we have to remove the ith indexed character from the string.

In any string, indexing always start from 0. Suppose we have a string geeks then its indexing will be as –

g e e k s
0 1 2 3 4
Examples :

Input : Geek
        i = 1
Output : Gek

Input : Peter
        i = 4
Output : Pete
"""


def remove_by_index(string, index):
    if index not in range(len(string)):
        return string
    return string[:index] + string[index + 1:]


print(remove_by_index("", 3))