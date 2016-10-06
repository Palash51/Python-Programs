#general
'''lnum = int(raw_input("enter the lower limit: "))
unum = int(raw_input("enter the upper limt: "))
sum = 0
for i in range(lnum, unum+1):
    sum = sum + i

print sum
'''

#using function
'''
def sum(x,y):
    count = 0
    for i in range(x, y+1):
        count  = count + i
    return count


print sum(1,10)
'''

#recursive

def sum(x, max):
    if x == max:
        return max
    return x + sum(x+1, max)
print sum(1, 10)
