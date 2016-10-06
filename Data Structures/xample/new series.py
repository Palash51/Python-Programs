case = int(raw_input())
for i in range(case):
	x, y, z = [int (i) for i in raw_input ().split ()]
	total = 0
	num = [y]*x
	for j in range(x,z):
		for m in range(x):
			total = total + num[j-(m+1)]
		num.append(total)
		total = 0
	print num[z-1] 