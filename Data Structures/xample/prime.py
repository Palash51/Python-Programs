'''def prime_num(num):
    print "1",
    for i in range(2,num):
        j = 2
        count = 0
        while j < i:
            if i%j == 0:
                count = 1
                break
            else:
                j += 1
        if count == 0:
        	print num,	      
         
            
prime_num(20)'''
def count_prime(x):
    if x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                return False
                break
        else:
            return "TRUE"
    else:
        return "FALSE"

print count_prime(7)
'''def relative_prime(number):
    count = 0
    for j in range(1, number):
        if number%j != 0:
            count += 1
    return count + 1
print relative_prime(5)'''
