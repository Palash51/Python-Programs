'''def seqsearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found :
        if alist[pos] == item:
            found = True

        else:
            pos = pos + 1

    return found

tlist = [1, 2, 32, 8, 17, 19, 42, 38, 0]
print(seqsearch(tlist, 32))
#print(seqsearch(tlist, 3))
'''

def seqsearch(alist, value):
    for i in range(len(alist)):
        if alist[i] == value:
            return i

    return -1

A = [62,656,65,9,98,41,77,0]
print(seqsearch(A, 100))
