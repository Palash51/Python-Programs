def arr_sort(A):
	zeroth = []
	ones = []
	two = []
	for i in range(len(A)):
		if A[i] == 0:
			zeroth.append(A[i])

		elif A[i] == 1:
			ones.append(A[i])

		else:
			two.append(A[i])

	s_list = zeroth + ones + two
	return s_list

A = [0,1,1,0,1,2,1,2,0,0,0,1]
print arr_sort(A)

