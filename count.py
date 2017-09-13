 
#j = 0
def calll(a):
	x = len(a)
	b = [0]*x
	y = len(b)
	i = 0	
	c = 0
	def ch(a):

		while(x>0):
			if a[i]>0:
				b[i] = 1
			
			i = i + 1
			x = x-1
			c = c + 1
		j = 1
		while(b[j-1] != a[j-1]):

			if(a[j-1] - 1)%2 != 0:
				print a[j-1]
				b[j-1] = b[j-1]*2
			else:
				print ch(a)
		j = j + 1


		print b,c
			

a = [2,3]
	
print calll(a)

















# # a = [2,3]
# # c = 0
# # for i in range(len(a)):
# # 	if a[i]  % 2 == 0:
# # 	 	a[i] = a[i]/2
# # 	c = c + 1
# # 	if a[]
# #   	#a[i] = a[i] - 1

# def check(a,n):
# 	res = 0
# 	while(n!= 0):
# 		z = 0
# 		for i in range(n):
# 			if a[i] & 1:
# 				break
# 			elif(a[i] == 0):
# 				z = z + 1

# 		if z == n:
# 			return res

# 		if i == n:
# 			for j in range(n):
# 				a[j] = a[j]/2
# 			res = res + 1

# 		for j in range(i,n):					
# 			if a[j] & 1:
# 				a[j] = a[j] - 1
# 			res = res + 1
# 		n = n -1



# a = [16,16,16]
# n = len(a)
# print check(a,n)



