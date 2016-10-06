def count_prime(x):
    if x > 1:
        for i in range(2, x):
            if x%i == 0:
            	return "FALSE"
            	break
        else:
            return "TRUE"
    else:
        return "FALSE"
   
def relative_prime(number):
	count = 1
	for j in range(1, number):
		if number%j != 0:
			count += 1
	return count_prime(count)
	
n =int(raw_input())
#for i in range(n):
while n > 0:
	num = int(raw_input())
	print relative_prime(num)
	n -= 1