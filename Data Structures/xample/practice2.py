def prime_number(number):
	if number == 2:
		return none
	else:
		for i in range(2,number):
			if number%i != 0:
				return number
		

n = int(raw_input())
'''num_list = []
for i in range(n):
	num = int(raw_input())
	num_list.append(num)
num_string = list(num_list)'''
arr = [int(x) for x in raw_input().split()]
for j in arr:
	print prime_number(j)
	