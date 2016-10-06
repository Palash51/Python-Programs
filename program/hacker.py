t = input()

for i in range(t):
	inp = list(map(int, raw_input().split()))
	for j in range(1,inp):
		if j % 3 == 0 and j % 5 == 0:
			print "FizzBuzz"
		elif j % 3 == 0:
			print "Fizz"
			
		elif j % 5 == 0:
			print "Buzz"
		
		else:
			print j
			
			
