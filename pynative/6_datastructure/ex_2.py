"""
Exercise 2: Given a list, remove the element at index 4 and add it to the 2nd position and at the end of the list
Given:

list1 = [54, 44, 27, 79, 91, 41]
Expected Output:

Original list  [34, 54, 67, 89, 11, 43, 94]
List After removing element at index 4  [34, 54, 67, 89, 43, 94]
List after Adding element at index 2  [34, 54, 11, 67, 89, 43, 94]
List after Adding element at last  [34, 54, 11, 67, 89, 43, 94, 11]
"""


def remove_by_index(items: list, index: int) -> list:
    if index < len(items):
        items.remove(items[index])
    return items


def append_by_index(items: list, index: int, item):
    if index < len(items):
        items = items[:index] + [item] + items[index:]
    return items


original = [34, 54, 67, 89, 11, 43, 94]
print("Original ", original)


itms = remove_by_index(original, 4)
print("List After removing element at index 4", itms)

itms = append_by_index(original, 2, 11)
print(itms == [34, 54, 11, 67, 89, 43, 94])

# ###############################
sampleList = [34, 54, 67, 89, 11, 43, 94]

print("Original list ", sampleList)
element = sampleList.pop(4)
print("List After removing element at index 4 ", sampleList)

sampleList.insert(2, element)
print("List after Adding element at index 2 ", sampleList)

sampleList.append(element)
print("List after Adding element at last ", sampleList)