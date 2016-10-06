def stress(numb):
	t = 1
	while True:
		tm = numb[0]*(t ** 3) + numb[1]*(t ** 2) + numb[2]*(t) + numb[3]
		if tm < numb[4]:
			t += 1
		else:
			return t
			False
			
test = int(raw_input())
num = []
for i in range(test):
	n = raw_input()
	num.extend([int(i) for i in n.split(" ")])
	print stress(num)
	num = []
