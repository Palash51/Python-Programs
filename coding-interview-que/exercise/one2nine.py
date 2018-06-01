# def a(e,i):
#  if i<=9:
#  	[a(e+x+`i`,i+1)for x in("+","-","")]
#  elif eval(e)==100:
#  	print(e)

# print(a("1",2))



# print(len(new))

# import itertools
# for p in itertools.permutations(range(1,10)):
#     if p[0] < p[-1]:
#         print(p)

# def subset_sum(numbers, target, partial=[]):
#     s = sum(partial)

#     if s == target:
#         print("sum(%s)=%s" % (partial, target))
#     if s >= target:
#         return 

#     for i in range(len(numbers)):
#         n = numbers[i]
#         remaining = numbers[i + 1:]
#         subset_sum(remaining, target, partial + [n])



# subset_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 10)


# perm = ''.join(permutations([1,2,3,4,5,6,7,8,9], 7))
# l = list(perm)
# print(l)



# from itertools import *
# new = []
# for i in product(('+','-',''),repeat=8):
# 	s=''.join(''.join(j)for j in chain(izip_longest(map(str,range(1,10)),i,fillvalue='')))
# 	new.append(s)
# 	if eval(s)==100:
# 		print(s)



# from itertools import permutations

# p = permutations([1,2,3])

# new = []

# for i in list(p):
# 	new.append(list(i))

# sum = 0
# for x in new:
# 	sum = sum + int(''.join(str(e) for e in x))
	
# print(sum)




# def getall(s,n,res):
# 	if s == '':
# 		if n == 0:
# 			print(res)

# 	for i in range(1,len(s)):
# 		tmp = int(s[0:i])
# 		# print(type(s[i:]))
# 		# print(res + '+' + tmp)
# 		getall(s[i:], n-tmp, res + '+' + str(tmp))

# 		getall(s[i:], n+tmp, res + '-' + str(tmp))

# 		# recurse(string.substr(i), remaining - tmp, result + '+' + tmp);




# print(getall('123456789', 100, ''))




# def getcomb(lists):
# 	print(lists)
# 	# print(lists[:-1])
# 	# print(lists[-1])
# 	if lists == []:
# 		print("here")
# 		return [()]

# 	return [x + (y,) for x in getcomb(lists[:-1]) for y in lists[-1]]
	



# print(getcomb([['+','-','']]*8))
#,['+','-',''],['+','-',''],['+','-',''],['+','-',''],['+','-',''],['+','-',''],['+','-','']]))




# def product(ar_list):
#     if not ar_list:
#         yield ()
#     else:
#         for a in ar_list[0]:
#             for prod in product(ar_list[1:]):
#                 yield (a,)+prod

# print(list(product([[1],[2],[3]])))








# def product(*args, **kwds):
#     # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
#     # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
#     pools = map(tuple, args) * kwds.get('repeat', 8)
#     result = [[]]
#     for pool in pools:
#         result = [x+[y] for x in result for y in pool]
#     return result
#     # for prod in result:
#     #     yield tuple(prod)

# print((product('+', '-', '')))


# def minion_game(string):
# 	ch = ''
# 	for i in string:
# 		ch = ch + i
# 		get_occurrence(ch,string)

# def get_occurrence(ch,string):

# 	vowels = ['A','E','I','O','U']
# 	count = 0
# 	# if ch in vowels:
# 	count = string.count(ch)
# 	print(count,ch)







# s = input()
# minion_game(s)



# s, v = input(), 'AEIOU'

def minion_game(s):
	vowels = 'AEIOU'
	stuart = 0
	kevin = 0
	l = len(s)
	for i in range(l):  
		if s[i] in vowels:
			kevin += l - i
		else:
			stuart += l - i
        
	if stuart > kevin:
	    print('Stuart ', stuart)
	elif stuart == kevin:
	    print('Draw')
	else:
	    print('Kevin ', kevin)

minion_game("BANANA")