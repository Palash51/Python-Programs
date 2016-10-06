def maxSubArraySum(a,size):
     
    max_so_far =a[0]
    curr_max = a[0]
     
    for i in range(1,size):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far,curr_max)
         
    return max_so_far
 
# Driver function to check the above function 
a = [1,2,-1,3,4,10,10,-10,-1]
print"Maximum contiguous sum is" , maxSubArraySum(a,len(a))
