# list a way to group several values at the same time

colors = ['black', 'red', 'green', 'blue']

print(colors)

colors[0] = 'white'

colors.append("orange")
colors.remove("green")

print("colors.index = ", colors.index("white"))
colors.sort()
print("colors.index = ", colors.index("white"))

for color in colors:
    print(color)

print("red in colors: ", "red" in colors)
print("grey in colors: ", "grey" in colors)

print("Slice: ", colors[0:2])

print("------------------")

items = ['black', 1.5, True]

for item in items:
    print(item)

print(len(items))
