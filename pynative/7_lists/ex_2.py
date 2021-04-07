"""
Exercise 2: Concatenate two lists index-wise
Given:

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
"""

list1 = ["M", "na", "i", "Ke", "I am "]
list2 = ["y", "me", "s", "lly"]


def concatenate(items1, items2):
    if len(items1) == len(items2):
        result = [items1[index] + items2[index] for index in range(len(items1))]
        return result
    return []


def concatenate2(items1, items2):
    if len(items1) >= len(items2):
        items1 = items1[:len(items2)]
    result = [items1[index] + items2[index] for index in range(len(items1))]
    return result


print(concatenate(list1, list2))
print(concatenate2(list1, list2))


res = [value1 + value2 for value1, value2 in zip(list1, list2)]

print(res)