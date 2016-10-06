#import string
num = input()

new = []

while num > 1:
    rem = num % 2
    new.append(rem)
    num = num / 2
    if num == 1:
        new.append(num)
    
print new

#b = ''.join(str(e) for e in new)
#print b

#count = 0
'''
for i in range(0,len(new)+1):
    i = 0
    count = 1
    if new[i] == 1:
        for j in range(i+1,len(new)):
            if new[i] == new[j]:
                count = count + 1
            i = i + 1
'''
'''
if new[i] == 1
        count = 1
        if new[i-1] == new[i]:
            count = count + 1
            i = i + 1
    #i = i + 1
'''
#print count
   
def myFun(n):
    
    for i in range(0,len(n)):
        count = 0
        if n[i] == 1:
            i = 0
            if n[i] == n[i+1]:
                count = count + 1
                
            #print n[i]
            
            #for j in range(i+1,len(n)):
             #   if n[i] == n[j]:
              #      count = count + 1
    print count
myFun(new)
 









