def sen_rev(strng):
	new_str = []
	for char in strng:
		if ' ' in strng:
			new_str.append(char)

	return new_str

sen_rev("palash patidar")
