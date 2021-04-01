"""

Exercise 4: Given a string and an integer number n,
remove characters from a string starting from zero up to n and return a new string
"""


def slice_text(text: str, n: int):
    return text[n:]


print(slice_text(text="testing", n=4))

# website sol is the same
