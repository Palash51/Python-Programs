num = int(input('enter the number'))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print('not a prime number',num)
            print(i,"times",num//i,"is",num)
            break
        else:
            print('prime number {}'.format(num))

else:
    print('not a prime number {}'.format(num))
