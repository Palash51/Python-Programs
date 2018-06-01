def large_cont_sum(arr):

	if len(arr) == 0:
		return 0

	current_sum = arr[0]
	max_sum = current_sum
	

	for num in arr[1:]:

		current_sum = max(current_sum + num, num)
		max_sum = max(current_sum,max_sum)

	print max_sum


large_cont_sum([1,2,-1,3,4,10,10,-10,-1])
