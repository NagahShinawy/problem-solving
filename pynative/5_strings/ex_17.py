import re
"""
Exercise 17: Find words with both alphabets and numbers
Given:

str1 = "Emma25 is Data scientist50 and AI Expert"
Expected Output:

Emma25
scientist50
"""


def contains_number(word):
    word = (char.isdigit() for char in word)
    return any(word)


def contains_number2(word):
    return True if re.search(r"\d", word) else False


str1 = "Emma25 is Data scientist50 and AI Expert"
words = [word for word in str1.split() if word]
print(words)

words_with_numbers = [word for word in words if contains_number(word)]
print(words_with_numbers)


words_with_numbers = [word for word in words if contains_number2(word)]
print(words_with_numbers)


# ###################################


res = []
temp = str1.split()
for item in temp:
    if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
        res.append(item)

print("Displaying words with alphabets and numbers")
for i in res:
    print(i)