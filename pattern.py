'''def arevr(arr):
	arr.sort()
	print arr
	
def drevr(arr1):
	arr1.sort(reverse=True)
	return arr1
	  
print(arevr([2,3,4,1,5,6,7]))
print(drevr([2,3,4,1,5,6,7]))
'''

'''def revr(arr):
	arr.sort()
	arr1 = []

	for i in range(len(arr))
		for j in range(len(arr), -1):
			while arr[j] != arr[i]:
				arr1.append(arr[j] + arr[i])
			print arr1

				


revr([1,3,2,4,6,5,7])
'''
'''
def revr(arr):
	arr.sort()
	new = []
	a = len(arr)

	for i in range(a):
		if i < a//2:
			j = 2*i + 1
			arr[j] = arr[i]
			new.append(arr[j])
		else:
			j = (a-1-i)*2
			arr[j] = arr[i]
			new.append(arr[i])

	return new

print(revr([1,3,2,4,6,5,7]))


'''
arr = [1,2,3,5,6,7,12,8,11,10]
arr.sort()
n = len(arr)
i = n-1
j = 0
arr1 = []
while True:
	arr1.append(arr[i])
	
	if j < i:
		arr1.append(arr[j])
		j += 1
		if i == j:
			break
	else:
		break
	
	i -= 1

print arr1

