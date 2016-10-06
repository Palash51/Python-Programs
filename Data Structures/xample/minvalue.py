'''def min_fun(fun):
    return min(fun)

numsort = [7, 1 ,4, 2]
min_value = min_fun(numsort[1:len(numsort)])
print min_value'''


def swap(x, y):
    temp = x
    x = y
    y = temp
    return x, y

'''def min_fun(fun):
    return min(fun)'''

numsort = [7, 1 ,4, 2]
x = 3
for i in range(len(numsort)-1):
    #min_value = min_fun(numsort[1:len(numsort)])
    swap(x, numsort[i])
    print numsort
