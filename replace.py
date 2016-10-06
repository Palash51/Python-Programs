'''def strng(str):
	for i in range(len(str)):
		for j in range(i+1, len(str)):
			if str[j] == str[i]:
				a = 'r'
				while a in the str:
					str_new = str.replace(str[j], '$')

	return str_new'''

def strng(str):
	print len(str)
	str = list(str)
	arr = []
	i = 0
	j = i + 1
	#arr.append(str[0])
	for j in range(len(str)):
		if str[j] == str[i]:
				str[j] = '$'
				arr.append(str[j])
			#print str
		else:
			arr.append(str[j])
	print arr

strng("restart")
