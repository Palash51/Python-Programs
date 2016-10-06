def check(A):
    for i in range(0, len(A)):
        for j in range(i+1, len(A)):
            if(A[i] == A[j]):
                print("duplicate exist:", A[i])
                return;

    print("no duplicate")

A = [2,2, 3, 4, 5, 7]
check(A)
'''
def find_duplicate_hash(A):
    d = {}
    for index, item in enumerate(A):
        if d.hash_key(item):
            return item
        else:
            d[item] = True


A = [2,2, 3, 4, 5, 7]
find_duplicate_hash(A)
'''
