num = input()
lst = [int(i) for i in str(num)]
while 0 in lst:
    lst.remove(0)
#print lst
count = 0
for j in range(len(lst)):
    if num % lst[j] == 0:
        count = count + 1
        #print lst[j]
print count
