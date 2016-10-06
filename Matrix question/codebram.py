ncols = 2
nrows = 2
matrix = []
x = list(map(int,raw_input().split()))
print x
for i in range(nrows):
    matrix.append([i for j in x] * ncols)


print matrix
