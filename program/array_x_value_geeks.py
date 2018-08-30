CONST_MAX = 100000
def printpair(arr,val):
	binmap = [0]*CONST_MAX  #INITIALIZE ALL CELLS AS 0
	found = True
	for i in range(0,len(arr)):
		temp = val - arr[i]
		import pdb
		pdb.set_trace()
		if temp>=0 and binmap[temp]==1 and found == True:
			print arr[i],temp
		binmap[arr[i]] = 1
		if found == False:
			print "no"

A = [1,4,45,6,10,-8]
n = 16
printpair(A,n)






'''def arrx(alist,val):
	count = x
	for i in range(len(alist)-1):
		for j in range(i+1,len(alist)):
			if alist[i] + alist[j] == count:
				print alist[i],alist[j]


alist = [1,4,45,6,10,-8]
print arrx(alist,16)
'''