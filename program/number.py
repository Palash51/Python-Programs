from __future__ import division

#a = 123456
a = input()
b = str(a)
c = []
new = []
for digit in b:
    c.append (int(digit))

for i in range(len(c)):
    if c[i] == 0:
        c.remove(c[i])

print c
'''
for i in range(len(c)):
    if a % c[i] == 0:
        new.append(c[i])

print new

'''
