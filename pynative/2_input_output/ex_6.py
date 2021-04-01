"""
Exercise 6: Write all content of a given file into a new file by skipping line number 5
Given test.txt file:

line1
line2
line3
line4
line5
line6
line7
Expected Output:

line1
line2
line3
line4
line6
line7
"""

with open("test.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

new_lines = ""
for line in lines:
    if line == "line5":
        continue
    new_lines += line + "\n"

with open("test.txt", "w") as f:
    f.write(new_lines)


def skip_line5():
    with open("test.txt", "r") as fp:
        lines = fp.readlines()
        count = len(lines)
    with open("newFile.txt", "w") as fp:
        for line in lines:
            if count == 3:
                count -= 1
                continue
            else:
                fp.write(line)
            count -= 1
