a = [2,3,5,0,4]

for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j]>a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]

print a
