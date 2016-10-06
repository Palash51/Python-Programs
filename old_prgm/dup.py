def check(A):
    count = 0
    for i in range(0, len(A)):
        for j in range(1,len(A)-1):
            if A[i] % A[j] == 0:
                count = count + 1
                return
    
    if count>1:
        print "prime no"
    else:
        print "no"

A = [10, 3, 5, 2, 16]
check(A)
