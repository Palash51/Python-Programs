#inp = list(map(int,raw_input().split()))
#print inp
#print inp[1]
#b = string.join(inp)
#b = "".join(str(e) for e in inp)
#print b

#c = int(b)
#print c
#if c % 10 == 0:
 #   print "yes"
#n = input()
#inp = [int(i) for i in raw_input().strip().split()]

n, inp = input(), [int(i) for i in raw_input().strip().split()]
new = []
for i in range(0,len(inp)-1):
    if inp[i] > inp[i+1]:
        new.append(inp[i])

print new
b = "".join(str(e) for e in new)
print b



#n, data = input(), [int(i) for i in raw_input().strip().split()]
