'''num = input()
#temp = num
rev = 0
new =[]
for i in range(1,num):
    #while i > 0:
    rev = rev * 10
    rev = rev + i % 10
    i = i / 10

if num == rev:
    new.append(rev)   

	#print "a palindrome"

print new
#else:
#	print "not a palindrom"


'''
new = []
def num_palindromes(start, end):
    count = 0
    for i in range(start, end + 1):
        if str(i) == str(i)[::-1]:
            count += 1
            new.append(str(i))
    print new        
    return count

print num_palindromes(10,200)
