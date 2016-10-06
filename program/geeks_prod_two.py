n = input()
for i in range(n):
    num = input()
    p = int(input())
    l = list(map(int,raw_input().split()))
#l = [1,2,3,4,5]
    s =set()
    f = 0
    
    for i in l:
        if(p % i == 0):
            v = int(p/i)
        #c = c + 1
        if v not in s:
            s.add(i)
        else:
            print "YES"
            print(i,v)
            f = 1
            break

if f != 1:
    print "NOT FOUND"
