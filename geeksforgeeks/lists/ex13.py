"""
Python | Sum of number digits in List
The original list is : [12, 67, 98, 34]
List Integer Summation : [3, 13, 17, 7]
"""

res = []

lst = [12, 67, 98, 34]

for num in lst:
    total = 0
    for digit in str(num):
        total += int(digit)
    res.append(total)


print(res)

# ##############################
res = list(map(lambda ele: sum(int(sub) for sub in str(ele)), lst))

print(res)