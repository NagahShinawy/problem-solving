"""
Exercise 10: Read line number 4 from the following file
test.txt file:

line1
line2
line3
line4
line5
line6
line7
"""


def catch_line(line_number):
    with open("test.txt", "r") as f:
        lines = f.readlines()
    if line_number <= len(lines):
        return lines[line_number - 1]  # item 4 means index 3


print(catch_line(4))
print(catch_line(5))
print(catch_line(6))
