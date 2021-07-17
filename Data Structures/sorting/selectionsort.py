a = [2,3,8,5,0,1,9,7,4]

for i in range(len(a)):
    least = i 
    for j in range(i+1,len(a)):
        if a[j] < a[least]:
            least = j 
            
        
    temp = a[i]
    a[i] = a[least]
    a[least] = temp
    

print (a)
