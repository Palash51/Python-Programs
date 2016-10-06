'''def myFun(n):
    for i in range(0,3):
        print n[i]

myFun([3,5,7])
'''
'''
print len(''.join(str(bin(1)).split('0')))-1


def longRunZeros(s):
    return max(len(i) for i in s.split(1))

longRunZeros(13)
'''

num = input()
new = []

while num > 1:
    rem = num % 2
    new.append(rem)
    num = num / 2
    if num == 1:
        new.append(num)
b = ''.join(str(e) for e in new)
print b
#binstr = '1101'
import re
zeros = re.compile(r'1+')
print max(len(m) for m in zeros.findall(b))
