n = raw_input()
num = []
num.extend([int(i) for i in n.split(" ")])
days = 1
x = num[0]
while True:
	if num[2] <= x:
		print days
		break
	elif num[2] == (x - num[1]):
		print days
		break
	else:	
		days += 1
		x = x + num[0] - num[1]

'''import math

A, B, N = [int (i) for i in raw_input ().split ()]
print int (math.ceil (1.0 * (N - B) / (A - B)))'''		