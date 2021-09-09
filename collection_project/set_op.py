colors = {'black', 'grey'}

print(colors)

for i in colors:
    print(i)

colors.add('white')
print colors

colors.discard('grey')

print("=========== Math & Sets ================")

colors1 = {'black', 'grey', 'red'}
colors2 = {'black', 'blue'}

print("Intersect: ", colors1 & colors2)
print("Union: ", colors1 | colors2)
print("Difference: ", colors1 - colors2)
print("Superset: ", colors1 > colors2)

item = set(("coffee", "tea", "black", "white"))
