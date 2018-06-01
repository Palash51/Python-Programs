num1 = input()
print("enter the first number")
num2 = input("enter the second number ")
if num1>num2:
    print("number 1 is greater than 2")
    max = num1
    min = num2
else:
    print("number 2 is greater then 1")
    max = num2
    min = num1
if max%min==0:
    print("hcf is %d" %(min))
    lcm = (num1*num2)/min
    print("lcm is %d" %(lcm))
   
else:
    r = max%min
    print("hcf is %d" %(r))
    lcm = (num1*num2)/r
    print("lcm is %d" %(lcm))
    
        

    
