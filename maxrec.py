m,n = map(int,raw_input('Enter Size:').split())
maze1=[]
for i in range(m):
	maze1.append(map(int,raw_input().split())) # [[1, 1, 0, 0], [0, 1, 0, 1], [0, 1, 0, 1], [1, 1, 0, 1]]


m,n = map(int,raw_input('Enter Size:').split())
maze2=[]
for i in range(m):
	maze2.append(map(int,raw_input().split())) # [[1, 1, 0, 0], [0, 1, 0, 1], [0, 1, 0, 1], [1, 1, 0, 1]]

res = [[0]*n]*2
print res
#print maze1,maze2
for i in range(len(maze1)):
	for j in range(len(maze1[0])):
		for k in range(len(maze2)):
			res[i][j] += maze1[i][k] * maze2[k][j]

		

print res
for r in res:
	print r