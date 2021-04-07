"""
Exercise 8: Iterate a given list and Check if a given element already exists in a dictionary as a key’s value if not delete it from the list
Given:

rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
sampleDict ={'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
Expected Outcome:

After removing unwanted elements from list [47, 69, 76, 97]
"""

numbers = [47, 64, 69, 37, 76, 83, 95, 97]
scores = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}
exits = []
removed = []
for num in numbers:
    if num in scores.values():
        exits.append(num)
    else:
        removed.append(num)

print(exits)
exits = [num for num in numbers if num in scores.values()]
print(exits)
print(removed)