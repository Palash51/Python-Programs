'''
def arrx(alist,val):
	count = val
	for i in range(len(alist)-1):
		for j in range(i+1,len(alist)):
			if alist[i] + alist[j] == count:
				print alist[i],alist[j] ,str(count)


alist = [1,4,45,6,10,-8]
arrx(alist,16)
'''


CONST_MAX = 100000
def printpair(arr,val):
	binmap = [0]*CONST_MAX  #INITIALIZE ALL CELLS AS 0

	for i in range(0,len(arr)):
		temp = val - arr[i]
		if temp>=0 and binmap[temp]==1:
			print "pair with the given sum",val, "is", arr[i], "and", temp
		binmap[arr[i]] = 1
    
	

A = [1,4,45,6,10,-8]
n = 100
printpair(A,n)


















