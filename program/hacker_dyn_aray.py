inp = (map(int,raw_input().split()))  #inp[0] = 2, inp[1] = 5
s1 = []
s2 =[]
lastAns = 0
new = []
seq = 0
ans = []
for j in range(inp[1]):
    q = (map(int,raw_input().split()))  # q[0] = 1 or 2 , q[1] = x , q[2] = y
    new.append(q)

#print new

for i in range(len(new)):
    if new[i][0] == 1:
        #print 'hola'
        seq = (new[i][1] ^ lastAns) % inp[0]
        #print seq
        if seq == 0:
            s1.append(new[i][2])
        elif seq==1:
            s2.append(new[i][2])



    else:
        seq = (new[i][1] ^ lastAns) %inp[0]
        if seq == 0:
            #print s1
            lastAns = s1[new[i][2] % len(s1)]
            #lastAns = s2[-1]
            #print lastAns

        else:
            lastAns = s2[new[i][2] % len(s2)]
            #print s2
            #print lastAns

    ans.append(lastAns)
    

#for k in ans:
   # print k
#print ans
        

#a = [0, 0, 0, 7, 3,0]
while 0 in ans:
    ans.remove(0)
for k in ans:
    print k
