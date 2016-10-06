
'''nums = []
n = input()
d = input()

nums.extend([int(i) for i in n.split(" ")])
print nums
#for i in range(len(nums))
 ##              if nums[j] + nums[i] % d == 0:
   #                     print nums[j],nums[i]
            

n = raw_input()
t = list(map(int(i) for i in n.split(" ")))
print t

'''



num = raw_input()
l = map(int, str(num))
print l

for i in range(0,len(num)):
    if l[i] == 0:
        del l[i]
print l
new = []
for i in range(len(l)):
    if str(num) % l[i] == 0:
        new.append(l[i])

print new


    
