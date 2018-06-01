def str1(str):
	if len(str) < 2:
		return ''
	else:
		return str[0:2] + str[-2:]

print str1("palash")