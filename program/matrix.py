'''m = input("rows")
n = input("colmn")

first = []
for i in range(m):
    for j in range(n):
        first[i][j] = input()


for i in range(m):
    for j in range(n):
        print first[i][j]
 
        
#'''
'''
nn_matrix = raw_input().split()
total_cells =  len(nn_matrix)
# calculate 'n'
row_cells = int(total_cells**0.5)
# calculate rows
matrix = [nn_matrix[i:i+row_cells] for i in xrange(0, total_cells, row_cells)]
'''



m = int(input('number of rows, m = '))
n = int(input('number of columns, n = '))

matrix = []

for i in range(0,m):
    m1 = input()
    matrix.append(m1)
    for j in range(0,n):
        n1 = input()
        matrix[i].append(n1)


print matrix
