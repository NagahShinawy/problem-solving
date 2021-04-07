
"""
Exercise 1: Below are the two lists convert it into the dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
Expected output:

{'Ten': 10, 'Twenty': 20, 'Thirty': 30}
"""


def create_dictionary(keys, values):
    return dict(zip(keys, values))


def create_dictionary2(keys, values):
    return {key: value for key, value in zip(keys, values)}


def create_dictionary3(keys, values):
    dic = dict()
    if len(keys) != len(values):
        return dic
    for index in range(len(keys)):
        key = keys[index]
        value = values[index]
        dic.update({key: value})
    return dic


print(create_dictionary(['Ten', 'Twenty', 'Thirty'], [10, 20, 30]))
print(create_dictionary2(['Ten', 'Twenty', 'Thirty'], [10, 20, 30]))
print(create_dictionary3(['Ten', 'Twenty', 'Thirty'], [10, 20, 30]))