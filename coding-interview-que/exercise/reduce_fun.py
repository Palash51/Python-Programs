from functools import reduce

r = reduce(lambda x,y: x+y, [4,7,2,11])
print(r)



def fact(n):
    if n == 0 or n == 1:
        return 1
    return fact(n-1) * n


def reduce_func(x,y):
    return x * fact(y)

lst = [1, 3, 1]
print(reduce(reduce_func, lst))



# def factorial(n):
#   return(reduce(lambda x,y:x*y,range(n+1)[1:]))

# print(factorial(5))