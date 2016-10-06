def compress(s):

	r = ""
	count = 1
	for i in range(1,len(s)):
		if s[i-1] == s[i]:
			count += 1
		else:
			r = r + s[i-1] +str(count)
			count = 1
		
	r = r + s[i-1] + str(count)

	return r

		#str1.append(s[i])

	#return str1


print compress("AAAaa")