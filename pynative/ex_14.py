"""
Exercise 14: Print downward Half-Pyramid Pattern with Star (asterisk)
* * * * *  
* * * *  
* * *  
* *  
*
"""

for i in range(6, 0, -1):
    for j in range(0, i - 1):
        print("*", end=" ")
    print()


print("#" * 50)


stars = 5
for i in range(5):
    for j in range(stars):
        print("*", end=" ")
    stars -= 1
    print()
