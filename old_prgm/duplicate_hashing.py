'''A = [1, 2, 3, 'a', 'b', 'c', 2, 3, 4, 'b', 'c', 'd']

unique = []
helperset = set()
for x in A:
    if x not in helperset:
        unique.append(x)
        helperset.add(x)

print(A)
print(unique)
'''
a, b = map(int, input().split())
