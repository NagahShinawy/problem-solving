"""
A permutation, also called an “arrangement number” or “order”, is a rearrangement of the elements of an ordered list S into a one-to-one correspondence with S itself. A string of length n has n! permutation.

Examples:

Input :  str = 'ABC'
Output : ABC
         ACB
         BAC
         BCA
         CAB
         CBA
"""

from itertools import permutations


def show_permutation(text: str):
    for perm in permutations(text):
        print("".join(perm))


show_permutation("ABC")