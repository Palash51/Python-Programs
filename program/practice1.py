'''arr1 = [1,5,9,10,15,20]
arr2 = [2,3,8,13]

arr_final = arr1 + arr2
print arr_final

first = []
#for i in range(len(arr_final)):
while len(arr_final) < 0:
    
    while len(first) < len(arr1):
        first.append(arr_final[i])

print first
'''

def merge(a, b):
	"""
	a and b are two sorted lists
	"""
	i = 0
	j = 0
	c =  []
	while i < len(a) and j < len(b):
		if a[i] < b[j]:
			c.append(a[i])
			i += 1
		else:
			c.append(b[j])
			j += 1
	if i < len(a):
		while i < len(a):
			c.append(a[i])
			i += 1
	if j < len(b):
		while j < len(b):
			c.append(b[j])
			j += 1
	print c[0:len(a)]
	print c[len(a):]
	return c

print merge([1,5,9,10,15,20], [2,3,8,13])











