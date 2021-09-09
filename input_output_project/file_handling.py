
file = open("reamme.txt", "r")

data1 = file.read()
print(data1)

data2 = file.read(10)
print(data2)


file.close()
