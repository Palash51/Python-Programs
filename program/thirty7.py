#import string
n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

l = arr[::-1]
b = ' '.join(str(e) for e in l)
print b
