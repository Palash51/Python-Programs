def sel_sort(A):
	for i in range(len(A)):
		least = i
		for j in range(i+1,len(A)):
			if A[j] < A[least]:
				least = j
		temp = A[i]
		A[i] = A[least]
		A[least] = temp


#		swap(A,least,i)
                

#def swap(A,x,y):
#	temp = A[x]
#	A[x] = A[y]
#	A[y] = temp

A = [1,3,8,4,2,5,9,7]
fun = sel_sort(A)
#print fun
print A
