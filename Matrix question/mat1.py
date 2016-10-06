'''
matrix = [  [5,4,7,11],[3,3,8,17]  ]
row=0
while row<2:
    col=0
    while col<4:
        print matrix[row][col]
        col=col+1
    row=row+1
'''
'''

def matrixmult (A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    if cols_A != rows_B:
      print "Cannot multiply the two matrices. Incorrect dimensions."
      return

    # Create the result matrix
    # Dimensions would be rows_A x cols_B
    C = [[0 for row in range(cols_B)] for col in range(rows_A)]
    print C

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    return C

print matrixmult([[1,1],[1,2]],[[1,2],[1,2]])

'''


'''
Matrix={}
for i in range(0,2):
  for j in range(0,2):
    Matrix[i,j] = raw_input("Enter the matrix:")

print Matrix
'''
'''
def initialize_twodlist(value):
    list=[]
    for row in range(n):
        list.append([value]*m)
    return list


n = input("num")
m = input("col")
value = input()
print initialize_twodlist(value)


'''
'''
nn_matrix = raw_input().split()
total_cells =  len(nn_matrix)
# calculate 'n'
row_cells = int(total_cells**0.5)
# calculate rows
matrix = [nn_matrix[i:i+row_cells] for i in xrange(0, total_cells, row_cells)]
print matrix

'''
'''
#print a + b
#print [sum(i) for i in zip(*a)]
result = [[0,0],[0,0]]
#result = []
for i in range(len(a)):
   # iterate through columns
   for j in range(len(b[0])):
       for k in range(len(b)):
           result[i][j] += a[i][k] + b[k][j]

#print result
for r in result:
   print(r)


'''
'''
t = int(raw_input())
m = []
new = []
for i in range(t):
    n = map(int, raw_input().split())
    #k = input()
    for i in range(n[0]):
        m.append(raw_input())
    new.append(m)
print new
'''

import re
import collections
import string

def r_shift(c_r):
	rhc = re.sub('\.',' ',c_r)
	c = rhc.replace(" ","")
	o_l = len(c_r)-len(c)
	p = "."*o_l+c
	return (p)
	#print p
def check_vert(s_fted,k):
	for i in range(len(s_fted)):
		for j in range(len(s_fted)):
			return
def check_horz(s_fted,k):
	return()
def check_diag(s_fted,k):
	return()

a =  int(raw_input())
for i in range(a):
	b =  map(int, raw_input().split())
	m = []
	s_fted = []
	for j in range(b[0]):
		m.append(raw_input())
	for k in m:
		s_fted.append(r_shift(k))
	print s_fted

print p
































