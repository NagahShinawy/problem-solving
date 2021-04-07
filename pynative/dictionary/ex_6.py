
"""
sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
keysToRemove = ["name", "salary"]

Expected output:

{'city': 'New york', 'age': 25}
"""


def remove_keys(dic, keys):
    result = dict()
    for key in dic:
        if key not in keys:
            result.update({key: dic[key]})
    return result


def remove_keys2(dic, keys):
    for key in keys:
        dic.pop(key, None)
    return dic


sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"

}
keysToRemove = ["name", "salary"]
print(remove_keys(sampleDict, keysToRemove))
print(remove_keys2(sampleDict, keysToRemove))
city = sampleDict.pop("city", None)  # return removed value or None

print("City", city)


sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
keysToRemove = ["name", "salary"]

sampleDict = {k: sampleDict[k] for k in sampleDict.keys() - keysToRemove}
print(sampleDict)
