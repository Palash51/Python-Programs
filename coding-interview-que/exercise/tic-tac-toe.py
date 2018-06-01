n = int(input().strip())
a = [[0]*n for _ in range(n)]
for i in range(n):
    a[i] = [int(j) for j in input().strip().split(" ")]

check = False
count = 1
new = []
c = 1
for i in range(len(a)):
	if (len(set(a[i])) == 1):
		check = True

	for j in range(1,len(a)):
		if a[j-1][i] == a[j][i]:
			count = count + 1

	if count == n:
		check = True
	count = 1

def get_diagonal(m, i0, j0, d):
    return [m[(i0 + i - 1)%len(m)][(j0 + d*i - 1)%len(m[0])]
                for i in range(len(m))]

d1 = (get_diagonal(a,-1,-1,-1))
d2 = (get_diagonal(a,1,1,1))

if (len(set(d1)) == 1) or (len(set(d2)) == 1):
		check = True


# b = [None] * (len(a) - 1)
# x = [b[:i] + r + b[i:] for i, r in enumerate([[c for c in r] for r in a])]
# new = [[c for c in r if not c is None] for r in zip(*x)]

# b = [None] * (len(a) - 1)
# x = [b[i:] + r + b[:i] for i, r in enumerate([[c for c in r] for r in a])]
# new = [[c for c in r if not c is None] for r in zip(*x)]

# for q in new:
# 	if len(q) == n:
# 		if (len(set(q)) == 1):
# 			check = True




print(check)
	

	# for j in range(len(a)):

	# 	new.append(a[i-1][j])
	# 	if a[i-1][j] == a[i][j]:
	# 		count = count + 1
	# if a[i-1][c] == a[i][c]:
	# 	count = count + 1
	# 	c = c + 1
	# check = False
	# count = 1
	# for j in range(len(a)):
	# 	c=i-1
	# 	print(c)
	# 	if a[i-1][c] == a[i][c]:
	# 		count = count + 1

	# 		#print(count)

	# if count == n:
	# 	check = True

# print(new)
# if count == n:
# 	check = True

	# for j in range(1,len(a)):
	# 	if (a[i][j-1] == a[i][j]):
	# 		j = j + 1

