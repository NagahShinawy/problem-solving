"""
Exercise 15: Remove special symbols/Punctuation from a given string
Given:

str1 = "/*Jon is @developer & musician"

Expected Output:

"Jon is developer musician"
"""

from string import ascii_letters
import re


letters = ascii_letters + " "
text = "/*Jon is @developer & musician"
result = ""
for letter in text:
    if letter in letters:
        result += letter


def remove_duplicated_spaces(sentence):
    sentence = " ".join(re.split(r"\s+", sentence, flags=re.UNICODE))
    return sentence


print(result)
print(remove_duplicated_spaces(result))