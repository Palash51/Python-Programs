def rev(strng):
	new = " "
	for i in range(len(strng), 0, -1):
		new = new + strng[i]

	return rev

print(rev('palash'))