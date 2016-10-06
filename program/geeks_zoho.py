def patt(a, n):
    new = []
    count = 0
    c = []
    for i in range(len(a)):
        while(a[i] > 3):
            new.append(3)
            count = count + 1
            temp = a[i] - 3
            a[i] = temp
            
        new.append(temp)
        count = count + 1
    c.append(count)

    print c
    print count
    #return new





t = input()
for i in range(t):
    a = list(map(int,raw_input().split()))
    n = input()
patt(a,n)
