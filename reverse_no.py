num = int(input("enter the number"))
reverse = 0
temp = num
while temp!=0:
    new = temp%10
    reverse = (reverse*10) + new
    temp = temp // 10

print("number is %d " %(reverse))
