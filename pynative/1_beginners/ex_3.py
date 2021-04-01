"""
Exercise 3: Given a string, display only those characters which are present at an even index number.
"""


def even_index_chars(text: str):
    even_chars = ""
    for i in range(len(text)):
        if i % 2 == 0:
            even_chars += text[i]

    return even_chars


# website sol
def even_index_chars_2(text: str):
    even_chars = ""
    for i in range(0, len(text), 2):
        even_chars += text[i]
    return even_chars


print(even_index_chars("testing"))
print(even_index_chars_2("testing"))
print(even_index_chars_2("pythonfor2"))
