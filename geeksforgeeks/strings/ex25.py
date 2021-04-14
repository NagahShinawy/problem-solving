"""
Given two sentences as strings A and B. The task is to return a list of all uncommon words.
A word is uncommon if it appears exactly once in any one of the sentences, and does not appear in the other sentence.

Note: A sentence is a string of space-separated words. Each word consists only of lowercase letters.

Examples:

Input : A = "Geeks for Geeks"
        B = "Learning from Geeks for Geeks"
Output : ['Learning', 'from']

Input : A = "apple banana mango"
        B = "banana fruits mango"
Output : ['apple', 'fruits']
"""


def find_uncommonwords(text1: str, text2: str):
    text1 = set([word.strip() for word in text1.split()])
    text2 = set([word.strip() for word in text2.split()])
    return text1 ^ text2


print(find_uncommonwords("python for ML", "python for web development"))
print(find_uncommonwords("Geeks for Geeks", "Learning from Geeks for Geeks"))
print(find_uncommonwords("apple banana mango", "banana fruits mango"))


def UncommonWords(A, B):
    # count will contain all the word counts
    count = {}

    # insert words of string A to hash
    for word in A.split():
        count[word] = count.get(word, 0) + 1

    # insert words of string B to hash
    for word in B.split():
        count[word] = count.get(word, 0) + 1

    # return required list of words
    return [word for word in count if count[word] == 1]


# Driver Code
A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"

# Print required answer
print(UncommonWords(A, B))
