def ins_sort(A):
    for i in range(1,len(A)):    
        j = i                    
        while j > 0 and A[j] < A[j-1]: 
            temp = A[j]
            A[j] = A[j-1]
            A[j-1] = temp
            j=j-1 
    return A

A = [1,5,9,3,8,7,2]
print ins_sort(A)
