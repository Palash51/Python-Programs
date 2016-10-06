'''
print ("Pattern C")
for e in range (0,6):
    print( e * 'i' + (6-e) * ' ')
'''
'''
def pascal(n):
    r1, r2 = [1], [1, 1]
    degree = 1
    while degree <= n:
        print(r1)
        r1, r2 = r2, [1] + [sum(pair) for pair in zip(r2, r2[1:]) ] + [1]
        degree += 1

pascal(6)
'''

n = 5
for i in range(n):
    cprint '*' * n
 
