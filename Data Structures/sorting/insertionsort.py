import time
start_time = time.time()
a = [1,3,6,2,0,8,4]
for i in range(1,len(a)):
    j = i
    while(j > 0) and a[j] < a[j-1]:
    	#a[j],a[j-1] = a[j-1],a[j]
        temp = a[j]
        a[j] = a[j-1]
        a[j-1] = temp
        j = j - 1
print(a)

# n = 10
# for i in range(n,0,-2):
# 	print i
#print time.time() - start_time

#0.000999927520752
#0.00100016593933