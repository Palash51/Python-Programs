import string
t = input()
l = []
for j in range(0,t):
    new = ""
    new1 = ""
    strng = raw_input()
    for i in range(len(strng)):
        
        if i % 2 == 0:
            new += str(strng[i])
        else:
            new1 += str(strng[i])
    l.append(new + " " + new1)
    
#print l
b = string.join(l,'\n')
#s = ''.join(l)
print b
