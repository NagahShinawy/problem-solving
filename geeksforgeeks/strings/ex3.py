"""
Ways to remove i’th character from string in Python

The original string is : GeeksForGeeks
The string after removal of i'th character : GeksForGeeks
"""


def remove_char_by_index(string, index):
    if index < len(string):
        return string[:index] + string[index + 1:]


def remove_char_by_index2(string, index):
    res = ""
    for idx, char in enumerate(string):
        if idx != index:
            res += char

    return res


def remove_char_by_index3(string, index):
    return "".join([string[i] for i in range(len(string)) if i != index])


print(remove_char_by_index("GeeksForGeeks", 2))
print(remove_char_by_index2("GeeksForGeeks", 2))
print(remove_char_by_index3("GeeksForGeeks", 2))
