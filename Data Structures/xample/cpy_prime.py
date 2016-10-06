def selsort(a):
    for i in range(len(a)):
        m = min(a)
        swap(a, i, m)
    return a

def swap(arr, x, y):
    #temp = 0
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp
    #return arr, x , y

a = [7, 5, 4, 2]
print selsort(a)
   
