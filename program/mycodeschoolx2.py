import math
new = []
def perfect_sq(n):
    if n == int(math.sqrt(n)) ** 2 :
        new.append(1)

    else:
        new.append(n)

test = input()
for i in range(test):
    num = input()
    perfect_sq(num)

#print new
for ele in new:
    print ele
