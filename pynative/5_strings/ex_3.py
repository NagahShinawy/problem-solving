"""
Exercise Question 3: Given two strings, s1, and s2 return a new string made of the first, middle, and last characters each input string

Given:

s1 = "America"
s2 = "Japan"
Expected Output:

AJrpan
"""


def get_middle(string):
    if len(string) % 2 == 0:
        index = len(string) / 2
        middle_chars_for_string = string[index - 1 : index]
    else:
        index = len(string) // 2
        middle_chars_for_string = string[index]

    return middle_chars_for_string


def merge_chars(first_string, second_string):
    merge_first_chars = first_string[0] + second_string[0]

    middle_for_first = get_middle(first_string)
    middle_for_second = get_middle(second_string)

    middle = middle_for_first + middle_for_second

    merge_last = first_string[-1] + second_string[-1]
    merge_all = merge_first_chars + middle + merge_last
    return merge_all


def mix_string(s1, s2):
    first_char = s1[:1] + s2[:1]
    middle_char = (
        s1[int(len(s1) / 2) : int(len(s1) / 2) + 1]
        + s2[int(len(s2) / 2) : int(len(s2) / 2) + 1]
    )
    last_char = s1[len(s1) - 1] + s2[len(s2) - 1]
    res = first_char + middle_char + last_char
    print("Mix String is ", res)


s1 = "America"
s2 = "Japan"
mix_string(s1, s2)

x = merge_chars("America", "Japan")
print(x)
assert x == "AJrpan"
