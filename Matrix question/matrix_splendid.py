'''
n=raw_input()
n=int(n)
size=pow(2,n)
matlist=[[1 for x in range(size)] for x in range(size)] 
def gen(n,s,a,b):
	i=0
	#print "gen(n,s,a,b)%i,%i,%i,%i",n,s,a,b
	if n>1:
		p=pow(2,n-1)*pow(2,n-1)
		k=pow(2,n)/2
		gen(n-1,s,a,b)
		#print '****** after first *****'
		gen(n-1,s+p,a,b+k)
		
		#print '****** after second *****'
		gen(n-1,s+p*2,a+k,b)
		#print '****** after third *****'
		gen(n-1,s+p*3,a+k,b+k)
		#print '****** after fourth *****'
	if n==1:
		
		#print "matlist[%i][%i]=%",a,b,s
		#print "matlist[%i][%i]=%",a,b+1,s+1
		#print "matlist[%i][%i]=%",a+1,b,s+2
		#print "matlist[%i][%i]=%",a+1,b+1,s+3
		matlist[a][b]=s
		matlist[a][b+1]=s+1
		matlist[a+1][b]=s+2
		matlist[a+1][b+1]=s+3
 
gen(n,1,0,0)
i=0
while(i<size):
	print ' '.join(map(str, matlist[i]))
	i=i+1
 
'''







ncols = 2
nrows = 2
matrix = []
x = list(map(int,raw_input().split()))
print x
for i in range(nrows):
    matrix.append([i for j in x] * ncols)


print matrix



 
