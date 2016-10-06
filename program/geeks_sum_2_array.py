#define function to reduce the code size

a = [9,2,3,7,9,6]
b = [3,1,4,7,8,7]
new = []
i = 0
j = 0
#alen = len(a)
#blen = len(b)
if len(a) < len(b):
    while(i<len(a)):
        sum = a[i] + b[j]
        if sum > 9:
            r = sum % 10
            new.append(1)
            new.append(r)
        else:
            new.append(sum)

        i = i + 1
        j = j + 1

    for k in range(len(a),len(b)):
        new.append(b[k])

else:
    while(i<len(b)):
        sum = a[i] + b[j]
        if sum > 9:
            r = sum % 10
            new.append(1)
            new.append(r)
        else:
            new.append(sum)

        i = i + 1
        j = j + 1

    for k in range(len(b),len(a)):
        new.append(a[k])

    
print new
