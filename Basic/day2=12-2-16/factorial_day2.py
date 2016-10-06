num = int(input("enter a num"))

fact = 1

if num < 0:
    print("sry factorial can not be generated")
elif num == 0:
    print("fact of 0 is 1")
else:
    for i in range(1, num+1):
        fact = fact*i

    print("the fact of",num, "is", fact)
