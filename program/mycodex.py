s = input()
new = []
for i in range(s):
    n = raw_input()
    inp = list(map(int,raw_input().split()))
    #print inp
    count = 0
    for k in range(len(inp)-1,0,-1):
        for j in range(k):
            if inp[j] > inp[j+1]:
                temp = inp[j]
                inp[j] = inp[j+1]
                inp[j+1] = temp
                count = count + 1

    new.append(count)

#print new
for elem in new:
    print elem


