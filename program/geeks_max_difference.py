'''
arr = [2,3,10,6,4,8,1]

i = 0
while(i < len(arr)):
    mini = arr[i]
    if arr[i+1] < arr[i]:
        mini = arr[i+1]
        i = i + 1
        
    i = i + 1
    

print mini
'''

'''
def maxDiff(arr1):
    max_diff = arr1[1] - arr1[0]

    for i in range(len(arr1)):
        for j in range(i+1,len(arr1)):
            if arr1[j] - arr1[i] > max_diff:
                max_diff = arr1[j] - arr1[i]

    return max_diff

arr1 = [2, 3, 10, 6, 4, 8, 1]

print maxDiff(arr1)
                                  
'''

def maxDiff(arr):
    max_diff = arr[1] - arr[0]
    min_ele = arr[0]
    for i in range(len(arr)):
        if arr[i] - min_ele > max_diff:
            max_diff = arr[i] - min_ele

        if arr[i] < min_ele:
            min_ele = arr[i]


    return max_diff


arr1 = [2, 3, 10, 6, 4, 8, 1]

print maxDiff(arr1)

