"""
Exercise 17: Find the sum of the series 2 +22 + 222 + 2222 + .. n terms
Given:

number_of_terms = 5
So series will become 2 + 22 + 222 + 2222 + 22222

Expected output:

24690
"""
limit = 5
total = 0
for i in range(1, limit + 1):
    total += int("2" * i)

print(total)

# another solution

total = 0
start = 2
for i in range(1, limit + 1):
    total += start
    start = (start * 10) + 2

print(total)
