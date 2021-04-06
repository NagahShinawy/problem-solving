"""
Exercise 13: Split a given string on hyphens into several substrings and display each substring
Given:

str1 = Emma-is-a-data-scientist
Expected Output:

Displaying each substring

Emma
is
a
data
scientist
"""

print(*"Emma-is-a-data-scientist".split('-'), sep="\n")

str1 = "Emma-is-a-data-scientist"
print("Original String is:", str1)

# split string
substrings = str1.split("-")

print("Displaying each substring")
for sub in substrings:
    print(sub)