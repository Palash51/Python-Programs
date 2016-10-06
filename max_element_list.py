def max_no(list):
	max = list[0]
	for i in list:
		if i > max:
			max = i

	return max

print(max_no([10,2,30,4,-4,-5,88]))