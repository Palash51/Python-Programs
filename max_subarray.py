def max_sub_array(arr,n):
	sub = []
	for i in range((len(arr)+1)-n):
		max_num = arr[i]
		for j in range(1,n):
			if arr[i+j] > max_num:
				max_num = arr[i+j]

		sub.append(max_num)

	return sub
arr = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
n = 3
print max_sub_array(arr,n)