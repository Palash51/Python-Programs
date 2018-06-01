# a = [1,2,5,7]
# s = sum(a)
# ele = []
# for i in range(1,s):
# 	

import  itertools
sum_list = []
stuff = [1,2,2,5,7]
for L in range(0, len(stuff)+1):
	for subset in itertools.combinations(stuff, L):
		print(subset)
		sum_list.append(sum(subset))

print(sum_list)
new_list = list(set(sum_list))
print(new_list)
new_list.sort()
for each in range(0,new_list[-1]+2):
    if each not in new_list:
        print(each)
        break