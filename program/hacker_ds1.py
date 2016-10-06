n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
new = []
for i in range(len(arr)-1,-1,-1):
    new.append(arr[i])
    
#print new
b = " ".join(str(e) for e in new)
print b
