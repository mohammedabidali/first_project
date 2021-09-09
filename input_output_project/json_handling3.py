import json

trainee = {'fname': "Adam",'lname': "Smith",'group': "Eng-94",'year': 2021, "subscribed": True, "courses": None}
print("this is the dictionary format")
print(trainee)

print("this is the JSON object")
trainee_json_object = json.dumps(trainee)
print(trainee_json_object)
