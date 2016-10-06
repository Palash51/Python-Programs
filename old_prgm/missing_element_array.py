def two_arr(arr1, arr2):

	if len(arr1) == len(arr2):
		print "nothing is missing"

	for i in range(len(arr1)):
		for j in range(len(arr2)):
			if arr1[i] != arr2[j]:
				


two_arr([1,2,3,4,5,6,7], [2,4,6,1,3,7])