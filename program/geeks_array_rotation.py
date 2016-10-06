a = [1,2,3,4,5,6,7]
n = input()
new = []

#for i in range(len(a)-1):
while n < len(a):
    new.append(a[n])
    n = n + 1
        #i = i + 1
#print n

x = n - len(new)
for i in range(x):
    new.append(a[i])
    
print new
