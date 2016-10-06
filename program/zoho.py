str1 = "I went to chennai"
#str1 = "one two three"
'''
i = len(str1)-1
new = []
start = 0
for j in range(len(str1)-1,0,-1):
    #print j
    if str1[j] == ' ':
        #print j
        start = j + 1
        #print start
        new.append(str1[start:i+1])
        i = j-1
        #print i
#print new
b = " ".join(str(e) for e in new)
print b + ' ' + str1.split()[0]
#print b
'''
'''
count = 0
while(count <= 1):
    k = 0
    if str1[k] == ' ':
        print k
        #count = count + 1
            
    k = k + 1
    count = count + 1
    
#print  b + ' ' + str1[0:k]
'''
#print str1.split()[0]

count = 0
for i in range(len(str1)):
    if str1[i] == ' ':
        count = count + 1

#print count
new = []
for j in range(count+1):
    new.append(str1.split()[j])
p = new[::-1]
b = " ".join(str(e) for e in p)
print b
    
    


























