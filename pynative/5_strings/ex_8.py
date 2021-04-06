"""
Exercise 8: Find all occurrences of “USA” in a given string ignoring the case
Given:

str1 = "Welcome to USA. usa awesome, isn't it?"

Expected Outcome:
The USA count is: 2
"""


def find_occurrences(search: str, text: str) -> int:
    text = text.lower()
    search = search.lower()
    return text.count(search)


def find_words(search: str, text: str) -> int:
    text = text.lower().split()
    search = search.lower()
    return text.count(search)


# website solution
inputString = "Welcome to USA. usa awesome, isn't it?"
substring = "USA"
tempString = inputString.lower()
count = tempString.count(substring.lower())
print("The USA count is:", count)

print(find_occurrences("uSA", "Welcome to USA. usa awesome, isn't it?"))
print(find_words("test", "testing TeSt TEST xxx"))
print(find_occurrences("test", "testing TeSt TEST xxx"))
