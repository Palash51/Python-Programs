
arr1 = [1,3,4,5,7]
arr2 = [2,3,5,6]

same = []
diff = []

for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr1[i] == arr2[j]:
            same.append(arr1[i])

        j = j + 1

    i = i + 1

a =  arr1 + arr2
print unique(a)

print same
'''

def printunion(arr1,arr2):
    i = 0
    j = 0
    new = []
    while(i < len(arr1) and j < len(arr2)):
        if arr1[i] < arr2[j]:
            print arr1
            i = i + 1

        elif arr2[j] < arr1[i]:
            print arr2
            j = j + 1

        else:
            print arr2
            j = j + 1
            i = i + 1

    while i < len(arr1):
        print arr1
        i = i + 1

    while j < len(arr2):
        print arr2
        j = j + 1

    #return new




arr1 = [1,3,4,5,7]
arr2 = [2,3,5,6]

print printunion(arr1,arr2)        
'''