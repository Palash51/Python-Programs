def arr(alist, val):
	count = val
	for i in range(len(alist)):
		j = i +1
		for j in range(len(alist)):
			if alist[j] + alist[j+1] == count:
				return alist[j], alist[j+1]


print(arr([1,3,2,2], 4))
