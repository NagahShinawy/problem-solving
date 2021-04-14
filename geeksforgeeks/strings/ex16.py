"""
Python – Specific Characters Frequency in String List
Last Updated : 05 Sep, 2020
Given String list, extract frequency of specific characters in whole strings list.

Input : test_list = [“geeksforgeeks is best for geeks”], chr_list =  ['e', 'b', 'g', 'f']
Output : {‘g’: 3, ‘e’: 7, ‘b’: 1, ‘f’ : 1}
Explanation : Frequency of certain characters extracted.

Input : test_list = [“geeksforgeeks], chr_list = [‘e’, ‘g’]
Output : {‘g’: 2, ‘e’: 4}
Explanation : Frequency of certain characters extracted.
"""

from collections import Counter


def frequency_for_chars(text: str, chars: list) -> dict:
    counts = {char: count for char, count in Counter(text).items() if char in chars}
    return dict(sorted(counts.items(), key=lambda item: item[1]))


print(frequency_for_chars("geeksforgeeks is best for geeks", ['e', 'b', 'g', 'f']))