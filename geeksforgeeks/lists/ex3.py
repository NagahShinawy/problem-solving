"""
test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']
List after performing character swaps : ['efg', 'is', 'bGst', 'for', 'eGGks']
"""


def swapchars(strings: list, char1: str, char2: str):
    return [string.replace(char1, '-').replace(char2, char1).replace('-', char2) for string in strings]


test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']
print(swapchars(test_list, 'e', 'G'))