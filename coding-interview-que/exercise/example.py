some_list = [1, 4, 5, 6]
for item in some_list:
	print(item)
	if item < 4:
		some_list.remove(item)
print(some_list)