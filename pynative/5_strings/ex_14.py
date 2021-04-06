"""
Exercise 14: Remove empty strings from a list of strings
Given:

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
Expected Output:

Original list of sting
['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']

After removing empty strings
['Emma', 'Jon', 'Kelly', 'Eric']
"""


def remove_empty(strings: list) -> list:
    return [string for string in strings if string]


print(remove_empty(["Emma", "Jon", "", "Kelly", None, "Eric", ""]))


# With filter function as None, the function defaults to Identity function,
# and each element in random_list is checked if it's true or not.

names = list(filter(None, ["Emma", "Jon", "", "Kelly", None, "Eric", ""]))
print(names)
names = list(filter(lambda name: name, ["Emma", "Jon", "", "Kelly", None, "Eric", ""]))

print(names)