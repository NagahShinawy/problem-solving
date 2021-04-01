"""
Exercise 9: How to check file is empty or not
"""
with open("empty.txt", "r") as f:
    content = f.read().strip()
if not content:
    print("File is empty")

else:
    print("file has data", content, sep="\n")


def is_empty_file(filename):
    """"
    check if file is empty then return True else False
    """
    import os

    return os.stat(filename).st_size == 0


print(is_empty_file("empty.txt"))
