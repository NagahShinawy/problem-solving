"""
Examples :

Split the string into list of strings

Input : Geeks for Geeks
Output : ['Geeks', 'for', 'Geeks']


Join the list of strings into a string based on delimiter ('-')

Input :  ['Geeks', 'for', 'Geeks']
Output : Geeks-for-Geeks
"""


def join_words(text: str, sep='-'):
    return f"{sep}".join([word.strip() for word in text.split()])


print(join_words("Greeks for Greeks", sep="|"))
print(join_words("Greeks for Greeks"))