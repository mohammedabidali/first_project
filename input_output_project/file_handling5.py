
file = open("reamme.txt", "w") # r+ = read and write and overwrite a file, w+ = read and write and truncates the file (starts fresh)

# write function creates a new file or just overwrites a file that exists
data = file.write("This is a new line 03")

print(data)

file.close()
