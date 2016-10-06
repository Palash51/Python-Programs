n = input()
new = []
for i in range(n):
    num = raw_input()
    new.append(num)
#print new

for i in range(0,len(new)):
    #print new[i]
    if new[i] % i == 0:
        print "NOT PRIME"
    else:
        print "PRIME"
        
    

