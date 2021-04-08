"""
Exercise 9: Given a 8_dictionary get all values from the 8_dictionary and add them to a list but don’t add duplicates
Given:

speed ={'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
Expected Outcome:

[47, 52, 44, 53, 54]
"""


def values_to_list(months: dict) -> list:
    return list(set([value for value in months.values()]))


def values_to_list2(months: dict) -> list:
    result = []
    for value in months.values():
        if value not in result:
            result.append(value)
    return result


print(values_to_list(
        {
            "jan": 47,
            "feb": 52,
            "march": 47,
            "April": 44,
            "May": 52,
            "June": 53,
            "july": 54,
            "Aug": 44,
            "Sept": 54,
        }
    ))


print(values_to_list2(
        {
            "jan": 47,
            "feb": 52,
            "march": 47,
            "April": 44,
            "May": 52,
            "June": 53,
            "july": 54,
            "Aug": 44,
            "Sept": 54,
        }
    ))


