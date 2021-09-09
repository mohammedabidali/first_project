
file = open("reamme.txt", "r")

data = file.readline()

while data != '':
    print(data)
    data = file.readline(5)


file.close()
