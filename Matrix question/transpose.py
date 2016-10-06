m,n = map(int,raw_input('Enter Size:').split())
maze1=[]
for i in range(m):
	maze1.append(map(int,raw_input().split())) # [[1, 1, 0, 0], [0, 1, 0, 1], [0, 1, 0, 1], [1, 1, 0, 1]]
res = [[0,0,0],[0,0,0]]

for i in range(len(maze1)):
	for j in range(len(maze1[0])):
		res[j][i] = maze1[i][i]

print res