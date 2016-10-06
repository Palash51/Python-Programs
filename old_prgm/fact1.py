'''num = int(raw_input("enter the no"))
fact = num
for i in range(1,num):
    fact = fact*i
print fact
'''
'''
num = int(raw_input("enter the no"))
sum = 0
while num > 5:
    temp = num // 5
    num = temp
    sum = sum + temp
print sum
'''
'''
x = int(raw_input("enter the no"))
#arr = []
arr = [int(i) for i in raw_input().split()]
for i in range(len(arr)):
    if arr[i] % x == 0:
        None
    else:
        print arr[i]

'''
'''
for i in range(2, 20):
           for x in range(2, i): #Using nested loops to get numbers within first range
                     if i % x == 0: #Checking whether first number is divisible by second number
                             print i, "equals", x, "*", i/x
                             break
           else:
                     print i, "is a prime number"
'''

#x = int(raw_input("enter the no"))
#arr = []
arr = [int(i) for i in raw_input().split()]
for i in range(len(arr)):
    for j in range(1, i):
        if i % j == 0:
            print ""
        else:
            print arr[i]









