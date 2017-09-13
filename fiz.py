t = input()
new = []
for i in range(t):
	lst = list(map(int, raw_input().split()))
	
	for j in lst:
		for k in range(1,j+1):
			if k % 3 == 0 and k % 5 == 0:
				print "p"

			elif k % 5 == 0:
				print "q"

			elif k % 3 == 0:
				print "r"

			else:
				print k

