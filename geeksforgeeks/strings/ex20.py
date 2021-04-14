"""
A string is given and you have to find all the words (substrings separated by a space) which are greater than given length k.

Examples:

Input : str = "hello geeks for geeks
          is computer science portal"
        k = 4
Output : hello geeks geeks computer
         science portal
Explanation : The output is list of all
words that are of length more than k.

Input : str = "string is fun in python"
        k = 3
Output : string python
"""


def get_words(text: str):
    return [word.strip() for word in text.split()]


def words_len(words, length: int) -> dict:
    return {word: len(word) for word in words if len(word) > length}


def main():
    text = "I love coding with python, agree"
    words = get_words(text)
    words_by_len = words_len(words, 4)

    print(words_by_len)
    print(sorted(words_by_len.items(), key=lambda word: word[1]))
    print(sorted(words_by_len, key=words_by_len.get))  # = print(sorted(words_by_len, key=words_by_len.get))
    print(sorted(words_by_len.items()))


if __name__ == '__main__':
    main()

