from math import sqrt, ceil

def Squares(start, stop):
    new = []
    for i in range(start, stop+1):
        x = sqrt(i)
        if x == ceil(x):
            new.append(i)

    #return new
    for i in new:
        print i

start = input()
stop = input()

Squares(start, stop)
