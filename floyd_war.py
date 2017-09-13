m,n = map(int,raw_input('Enter Size:').split())
maze=[]
for i in range(m):
	maze.append(map(int,raw_input().split())) # [[1, 1, 0, 0], [0, 1, 0, 1], [0, 1, 0, 1], [1, 1, 0, 1]]

#print len(maze)

for i in range(m):
	for j in range(n):
		for k in range(j+1,n):
			if maze[i][j] < maze[i][k]:
				a = maze[i][j]
				maze[i][j] = maze[i][k]
				maze[i][k] = a

print maze