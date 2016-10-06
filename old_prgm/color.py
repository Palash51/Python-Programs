colors = ['red', 'green', 'blue', 'yellow']


#1#
for color in reversed(colors):
    print(color)

#2#
for i, color in enumerate(colors):
    print(i, "-->", colors[i])

#3#

names = ['pal', 'pat', 'mu']

for name, color in zip(names, colors):
    print(name, "-->", color)


#4#

for color in sorted(colors, reverse = True):
    print(color)


#5#
'''
blocks = []

for block in iter(partial(f.red, 32), ''):
    blocks.append(block)
'''
print("\n\n")

d = {'maths': 'blue', 'phy':'green', 'che': 'red'}

for k in d:
    print(k)

print("\n\n")

for k in d.keys():
    if k.startswith('r'):
        del d[k]
        print(k)










