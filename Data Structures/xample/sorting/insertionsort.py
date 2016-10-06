def insertion_sort(numsort):
	for i in range(len(numsort) - 1):
		j = i + 1
		while j > 0 and numsort[j-1] > numsort[j]:
			swap(numsort, j-1, j)
			j = j - 1
		j = 0
	print numsort	

def swap(arr, x, y):
	temp = arr[x]
	arr[x] = arr[y]
	arr[y] = temp
	return arr , x, y 		

nums = []
n = raw_input()
nums.extend([int(i) for i in n.split(" ")])
insertion_sort(nums)
 
