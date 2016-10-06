n = input()
d = input()
#for i in range(n):
inp = list(map(int,raw_input().split()))
print inp
count = 0
for i in range(0,len(inp)-1):
    #print i
    for j in range(i+1,len(inp)):
        #print j
        if (inp[i] + inp[j]) % d == 0:
            count = count + 1
    
print count
