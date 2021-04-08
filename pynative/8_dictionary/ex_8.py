

"""
Exercise 8: Rename key city to location in the following 8_dictionary
sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

Expected output:

{
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "location": "New york"
}

"""


def rename_key(dic: dict, old_key, new_key):
    if old_key in dic:
        dic.update({new_key: dic[old_key]})
        dic.pop(old_key)
    return dic


def rename_key2(dic: dict, old_key, new_key):
    if old_key in dic:
        dic[new_key] = dic.pop(old_key)


sampleDict = {
  "name": "Kelly",
  "age": 25,
  "salary": 8000,
  "city": "New york"
}

print(rename_key(dic=sampleDict, old_key="city", new_key="location"))
print(rename_key(dic=sampleDict, old_key="test", new_key="TEST"))
print(rename_key(dic=sampleDict, old_key="salary", new_key="money"))