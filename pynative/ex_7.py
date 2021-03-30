""""
Exercise 7: Return the count of sub-string “Emma” appears in the given string
Given:

str = "Emma is good developer. Emma is a writer"
Expected Output:

Emma appeared 2 times
"""


def count_word_in_text(text: str, word: str) -> int:
    words = text.split()
    count = 0
    for w in words:
        if w == word:
            count += 1
    return count


def count_word_in_text_2(text: str, word: str) -> int:
    return text.count(word)


def count_word_in_text_3(text: str, word: str, case_insensitive=False) -> int:
    if case_insensitive:
        text = text.lower()
        word = word.lower()
    return text.count(word)


print(count_word_in_text("Emma is good developer. Emma is a writer", "Emma"))
print(count_word_in_text_2("Emma is good developer. Emma is a writer", "Emma"))
print(
    count_word_in_text_3(
        "emma is good developer. Emma is a writer eMmA", "Emma", case_insensitive=True
    )
)
