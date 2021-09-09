import json

trainee = {'fname': "Adam",'lname': "Smith",'group': "Eng-94",'year': 2021}

print(trainee)

with open('trainee.json', 'w') as file:
    json.dump(trainee, file, indent = 4)
