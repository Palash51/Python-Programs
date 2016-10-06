def prime_num(num):
    for i in range(2,num):
        j = 2
        while j < i:
            if i%j !=0:
                j += 1
            else:
                break
        print j
         
            
prime_num(20)            
