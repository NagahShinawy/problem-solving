"""
Given a string, the task is to check if every vowel is present or not. We consider a vowel to be present
if it is present in upper case or lower case. i.e. ‘a’, ‘e’, ‘i’.’o’, ‘u’ or ‘A’, ‘E’, ‘I’, ‘O’, ‘U’ .
Examples :

Input : geeksforgeeks
Output : Not Accepted
All vowels except 'o' are not present

Input : ABeeIghiObhkUul
Output : Accepted
All vowels are present
"""


def is_contains_vowels(text: str) -> bool:
    vowels = "aeiou"
    txt = text.lower()
    return all([v in txt for v in vowels])


print(is_contains_vowels("ABeeIghiObhkUul"))
print(is_contains_vowels("geeksforgeeks"))
