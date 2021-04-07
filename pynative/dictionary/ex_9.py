

"""
Exercise 9: Get the key of a minimum value from the following dictionary
sampleDict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
Expected output:

Math
"""


def get_key_for_min_value(dic):
    key_for_min = None
    min_value = max(dic.values())
    for key, value in dic.items():
        if value < min_value:
            min_value = value
            key_for_min = key
    return key_for_min


sampleDict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
print(get_key_for_min_value(sampleDict))


sampleDict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
print(min(sampleDict, key=sampleDict.get))  # key=function

