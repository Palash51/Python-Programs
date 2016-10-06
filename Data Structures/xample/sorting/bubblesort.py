def bubble_sort(numsort):
	for i in range(len(numsort)):
		for j in range(len(numsort)-1):
			if numsort[j] >= numsort[j+1]:
				swap(numsort, j, j+1)
	return numsort
def swap(arr, x, y):
	temp = arr[x]
	arr[x] = arr[y]
	arr[y] = temp
	return arr, x, y

nums = []
n = raw_input()
nums.extend([int(i) for i in n.split(" ")])
print bubble_sort(nums)