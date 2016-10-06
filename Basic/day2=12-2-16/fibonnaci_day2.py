num = int(input("enter a no"))

n1 = 0
n2 = 1
count = 2

if num <= 0:
    print("please provide positive no")
elif num == 1:
    print("fibo seq is {0}".format(n1))
else:
    print("fibo seq:")
    print(n1,",",n2,end=', ')
    while count < num:
        nth = n1 + n2
        print(nth,end=' , ')
        n1 = n2
        n2 = nth
        count += 1
