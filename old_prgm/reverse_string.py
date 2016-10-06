#text = "palash patidar lives in chennai"
def reverse(text):
	rev = ""
	for i in text:
		rev = i + rev
	return rev

str1 = open('a.txt').read()
print(reverse(str1))

'''

p = []
n = int(input('enter no'))
p.append([for int(i) in i])
'''