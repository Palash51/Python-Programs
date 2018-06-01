#Sorting1234
#ginortS1324

# def get_sorted()

def get_all(inp):
	lowercase = ''
	upercase = ''
	digits = ''
	even, odd = '', ''
	for i in inp:
		if i.islower():
			lowercase = lowercase + i
		if i.isupper():
			upercase += i
		if i.isdigit():
			if int(i) % 2 == 0:
				even = even + i
			else:
				odd = odd + i
	digits = ''.join(sorted(odd)) + ''.join(sorted(even))

	lowercase = ''.join(sorted(lowercase))
	upercase = ''.join(sorted(upercase))
	print(lowercase+upercase+digits)




inp = input()
get_all(inp)