"""
We are given a list of pattern strings and a single input string. We need to find all possible close good enough matches of input string into list of pattern strings.

Examples:

Input : patterns = ['ape', 'apple',
                  'peach', 'puppy'],
          input = 'appel'
Output : ['apple', 'ape']
"""

from difflib import get_close_matches


def close_matches(patterns, word):
    print(get_close_matches(word, patterns))


def main():
    word = 'appel'
    patterns = ['ape', 'apple', 'peach', 'puppy']
    close_matches(patterns, word)


# Driver program
if __name__ == "__main__":
    main()