"""
Given the string, the task is to generate the same string using the random combination of special character, numbers, and alphabets.

Examples :

Input : GFG
Output :n4W
        mK7
        k1x
        q;;, !g
        .
        .
        .
        .
        .
        GF,
        GFf
        GFp
        GFG

Target matched after 167 iterations
"""
import random


def guess_lang(language):
    user_lang = input("Enter Your Fav Lang:")
    counts = 1
    while user_lang.lower() != language:
        user_lang = input("Try Again:")
        counts += 1
    return counts


def computer_choice():
    return random.choice(["python", "java", "php", "javascript", "ruby", "go"])


def main():
    lang = computer_choice()
    print(lang)
    counts = guess_lang(lang)
    print(f"You Win After '{counts}' times")


if __name__ == '__main__':
    main()