## x = 3
## range 100-250
## o/p 35


t = int(input())

for i in range(t):
	x = input()
	s = input()
	c = 0
	n = [int(p) for p in s.split()]
	for i in range(n[0]+1,n[1]):
		print(i)
		c += str(i).count(x)
			

	print(c)


