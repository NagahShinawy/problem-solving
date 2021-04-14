"""
Given a string, the task is to check if that string contains any special character (defined special character set).
If any special character found, don’t accept that string.

Examples :

Input : Geeks$For$Geeks
Output : String is not accepted.

Input : Geeks For Geeks
Output : String is accepted
"""

SPECIAL_CHARS = "[@_!#$%^&*()<>?\\/|}{~:]"


# type hinting
def is_accepted(text: str) -> bool:
    return all([False for char in SPECIAL_CHARS if char in text])


print(is_accepted("Geeks$For$Geeks"))
print(is_accepted("GeeksFor$Geeks"))
print(is_accepted("GeeksForGeeks&"))
print(is_accepted("GeeksForGeeks]"))
print(is_accepted("GeeksForGeeks["))
print(is_accepted("GeeksForGeeks"))

