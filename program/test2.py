'''num = input()
lst = [int(i) for i in str(num)]
#print lst
#b = lst.remove(0)
#print b
#count = 0


for i in range(len(lst)-1):
    if lst[i] == 0:
        del lst[i]
        print lst
    i = i + 1
#print lst
'''

'''
for j in range(len(lst)):
    if num % lst[j] == 0:
        count = count + 1
        print lst[j]

print count

'''
'''
num = input()
lst = [int(i) for i in str(num)]

x = 0
for x in lst:
    lst.remove(x)

print lst
'''

#x = [0, 2, 0, 3,4, 4, 0, 2, 3]
num = input()
lst = [int(i) for i in str(num)]
while 0 in lst:
    lst.remove(0)
print lst
