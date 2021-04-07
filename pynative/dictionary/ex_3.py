
"""
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
"""


def get_history_value(obj):
    try:
        return obj["class"]["student"]["marks"]["history"]
    except KeyError:
        return


sampleDict = {
   "class": {
      "student": {
         "name": "Mike",
         "marks": {
            "physics": 70,
            "history": 80
         }
      }
   }
}

history = get_history_value(sampleDict)
if history is not None:
    print(history)