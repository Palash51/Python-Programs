def selection_sort(numsort):
	for i in range(len(numsort)-1):
		min_value = min_fun(numsort[i:len(numsort)])
		if min_value <= numsort[i]:
			swap(numsort, min_value, i)
			print numsort
	return numsort		

def min_fun(fun):
        return min(fun)

def swap(arr, x, y):
	temp = x
	x = arr[y]
	arr[y] = temp
	return arr

'''def swap(x, y):
	temp = x
	x = y
	y = temp
	return x, y'''
'''def selection_sort(numsort):
	for i in range(len(numsort)):
		min_value = i
		for j in range(i + 1,len(numsort)):
			if numsort[min_value] > numsort[j]:
				swap(numsort, min_value, j)
	return numsort			

def swap(arr, x, y):
	temp = arr[x]
	arr[x] = arr[y]
	arr[y] = temp
	return arr, x, y'''

nums = []
n = raw_input()
nums.extend([int(i) for i in n.split(" ")])
print selection_sort(nums)
