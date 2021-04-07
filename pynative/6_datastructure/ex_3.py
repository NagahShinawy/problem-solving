"""
Exercise 3: Given a list slice it into 3 equal chunks and reverse each chunk

Given:

sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
Expected Outcome:

Original list  [11, 45, 8, 23, 14, 12, 78, 45, 89]
Chunk  1 [11, 45, 8]
After reversing it  [8, 45, 11]
Chunk  2 [23, 14, 12]
After reversing it  [12, 14, 23]
Chunk  3 [78, 45, 89]
After reversing it  [89, 45, 78]
"""
items = [11, 45, 8, 23, 14, 12, 78, 45, 89]
chunks = [(*items[i: i + 3], ) for i in range(0, len(items), 3)]
reverse = [chunk[::-1] for chunk in chunks]
print(chunks)
print(reverse)

# #######################################
