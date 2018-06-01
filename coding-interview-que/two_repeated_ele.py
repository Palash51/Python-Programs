'''
def tworep(A):
	#new = []
	for i in range(0,len(A)):
		for j in range(i+1,len(A)):
			if A[i] == A[j]:
				#new.append(A[i])
				print A[i]
			#j += 1

	#print new

A = [3,5,7,4,3,1,5]
#A = [4,2,4,5,2,3,1]
tworep(A)
'''

def twoHash(A):

	table = {}
	for element in A:
		if element in table and table[element] == 1:
			print element
			table[element] += 1

		elif element in table:
			table[element] += 1

		elif element != "":
			table[element] = 1
		else:
			table[element] = 0

A = [4,2,4,c5,2,3,1]
twoHash(A)