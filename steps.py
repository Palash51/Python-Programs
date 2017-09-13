a = [16,16,16]
c = 0
c1 = 0
#for i in range(len(a)):
i = 0
while a[i] >= 0:
	print a[i]
	if a[i] % 2 != 0:
		a[i] = a[i] - 1
		c = c + 1

	else:
		a[i] = a[i]/2
		#print a[i]
		c1 = c1 + 1

	i = i + 1
	print i

	


print c,c1




# 	e = lambda x: not x % 2 == 0
# 	r = filter(e,a)
# 	c = 0
# 	#print r
# 	for j in range(len(r)):
# 		r[i] = r[i]-1
# 		c = c + 1
# print r,c
#c = 0

# for i in range(len(a)):
# 	#print a[i]
# 	while a[i] != 0:
# 		if a[i] % 2 == 0:
# 			#print a[i]
# 			a[i] = a[i]/2
# 			print a[i]
# 			c = c + 1

# 		else:
# 			print a[i]
# 			a[i] = a[i] - 1
# 			print a[i]
# 			c = c + 1
# print c