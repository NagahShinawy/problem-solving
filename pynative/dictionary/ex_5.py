"""
Home » Python Exercises » Python Dictionary Exercise with Solutions
Python Dictionary Exercise with Solutions
Updated on: March 9, 2021 | Python Tags: Basics Python Python Exercises

TweetF  sharein  shareP  Pin
This Python dictionary exercise aims to help Python developers to learn and practice dictionary operations. Here I am providing 10 dictionary programs to help you in brushing coding skills. All questions are tested on Python 3.

A dictionary object is mutable in Python. Python dictionary contains the data in the form of key-value pairs. Each key is separated from its value by a colon (:). Python dictionary is the most widely used data structure, and a good understanding of dictionary operations is necessary.

Also Read:

Python Dictionaries
Python Dictionary Quiz

This Python dictionary exercise includes the followings: –

It contains 10 dictionary questions and solutions provided for each question.
Practice different dictionary assignments, programs, and challenges.
It covers questions on the following topics:

Python dictionary operations and manipulations
Python dictionary functions
Python dictionary comprehension
When you complete each question, you get more familiar with the Python dictionary. Let us know if you have any alternative solutions. It will help other developers.

Use Online Code Editor to solve exercise questions.

Exercise 1: Below are the two lists convert it into the dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
Expected output:

{'Ten': 10, 'Twenty': 20, 'Thirty': 30}

Show Solution
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

sampleDict = dict(zip(keys, values))
print(sampleDict)
 Run Online
Exercise 2: Merge following two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
Expected output:

{'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
Show Solution
Python 3.5+

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3 = {**dict1, **dict2}
print(dict3)
 Run Online
Other Versions

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)
 Run Online
Exercise 3: Access the value of key ‘history’ from the below dict
sampleDict = {
   "class":{
      "student":{
         "name":"Mike",
         "marks":{
            "physics":70,
            "history":80
         }
      }
   }
}

Expected output:

80

Show Solution
Exercise 4: Initialize dictionary with default values
Given:

employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}
Show Solution
employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}

resDict = dict.fromkeys(employees, defaults)
print(resDict)

# Individual data
print(resDict["Kelly"])
 Run Online
Exercise 5: Create a new dictionary by extracting the following keys from a below dictionary
Given dictionary:

sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}

Keys to extract

keys = ["name", "salary"]
Expected output:

{'name': 'Kelly', 'salary': 8000}
"""


def include_keys(dic: dict, keys):
    result = dict()
    for key in keys:
        value = dic.get(key)
        if value is not None:
            result.update({key: value})
    return result


def include_keys2(dic: dict, keys):
    return {key: dic[key] for key in keys if key in dic}


sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"

}
keys = ["name", "salary"]

print(include_keys(sampleDict, keys=keys))
print(include_keys2(sampleDict, keys=keys))