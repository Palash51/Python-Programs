'''
import itertools

stuff = [1, 2, 3]
for L in range(0, len(stuff)+1):
  for subset in itertools.combinations(stuff, L):
    print subset



import itertools
for values in itertools.permutations([1,2,1]):
    print (values)


import itertools
#print list(itertools.permutations(set([1,2,1])))
print list(itertools.combinations([1, 2, 1],3))
#[(1, 1, 1)]
'''


'''
def permute(num):
    res = []
    if len(num) == 2:

        res.append(num)
        num[0], num[1] = num[1], num[0]
        
        res.append(num)
    else:
        for i in range(0, len(num)):
            
            for perm in permute(num[0:i] + num[i+1:len(num)]):
                
                res.append([num[i]] + perm)

    return res

#count = 0
#x = permute([1, 2,3])
'''
'''
for p in x:
    print p[0],p[1]
    #b = "".join(str(e) for e in p)
    #print b
    count = count + 1

print count
'''
#print permute([1,2,1])










def permute_unique(nums):
        perms = [[]]
        for n in nums:
            new_perm = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    new_perm.append(perm[:i] + [n] + perm[i:])
                    
                    if i < len(perm) and perm[i] == n:
                        break
            perms = new_perm
        print perms
        x = perms.append(nums)
        print x
       

nums = [1, 2, 1]
permute_unique(nums)




























