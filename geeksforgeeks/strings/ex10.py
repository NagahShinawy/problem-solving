"""
Given a pair of non empty strings.
Count the number of matching characters in those strings (consider the single count for the character which have duplicates in the strings).

Examples:

Input : str1 = 'abcdef'
        str2 = 'defghia'
Output : 4
(i.e. matching characters :- a, d, e, f)

Input : str1 = 'aabcddekll12@'
        str2 = 'bb22ll@55k'
Output : 5
(i.e. matching characters :- b, 1, 2, @, k)
"""


def remove_duplicates(items):
    return set(items)


def find_match(text1: str, text2: str):
    if len(text1) <= len(text2):
        end = len(text1)
    else:
        end = len(text2)

    matches = remove_duplicates([text1[i] for i in range(end) if text1[i] in text2])
    return matches


print(find_match("hello", "world"))