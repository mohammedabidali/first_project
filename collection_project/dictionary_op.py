trainee = {'fname': "Adam",'lname': "Smith",'group': "Eng-94",'year': 2021}

# or

trainee = dict(fname= "Adam",lname= "Smith",group= "Eng-94",year= 2021)

print('fname: ', trainee['fname'])
print('lname:', trainee['lname'])
print('group: ', trainee['group'])
print('year: ', trainee['year'])

trainee['fname'] = 'Mark'
print('fname: ', trainee['fname'])

for i in trainee:
    print(i)

print("Printing keys using for loop with .keys()")
for i in trainee.keys():
    print(i)

for i in trainee.values():
    print(i)

for key, value in trainee.items():
    print(key, ' :', value)
