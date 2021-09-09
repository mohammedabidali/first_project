
file = open("reamme.txt", "r")

data = file.read(1)

while data != '':
    print(data)
    data = file.read(1)


file.close()
