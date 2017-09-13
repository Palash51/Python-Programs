# import sys


# m = int(raw_input().strip())
# s = map(int, raw_input().strip().split(' '))

# snew = set(s)
# print len(snew)
# if len(snew) == m:
#     print "YES"
# else:
#     print "NO"


#!/bin/python

import sys


n,p,q = raw_input().strip().split(' ')
n,p,q = [int(n),int(p),int(q)]
a = map(int, raw_input().strip().split(' '))
b = map(int, raw_input().strip().split(' '))
sum = 0
min = 0
for i in a:
	if i < 3:
		min = i
	sum = sum + i
for j in b:
	if j < min:
		min = j
	sum = sum + j

rem = sum % 3
if rem == 0:
	pass
if rem < min:
	print rem

else:
	print sum