# import math
# import os
# import random
# import re
# import sys
# from operator import itemgetter

# def get_sorted(arr,k):
# 	val = {}
# 	for index,y in enumerate(arr):
# 		val[index]=y[k]

# 	new = sorted(val.items(), key=itemgetter(1))
# 	indx = [x[0] for x in new]
# 	for k in indx:
# 		print(' '.join(map(str, arr[k])))
		
# if __name__ == '__main__':
#     nm = input().split()
#     n = int(nm[0])
#     m = int(nm[1])
#     arr = []
#     for _ in range(n):
#         arr.append(list(map(int, input().rstrip().split())))
#     k = int(input())
#     get_sorted(arr,k)


n = int(input())
lst = []
for _ in range(n):
	lst.append(list(map(int, input().rstrip().split())))

print(lst)