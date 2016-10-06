def swap(arr, x, y):
	temp = x
	x = arr[y]
	arr[y] = temp
	print arr 
    
a = [1 , 2, 3]
value = 5
i = 0
swap(a, value, i)
