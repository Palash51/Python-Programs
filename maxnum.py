#a = [1, 34, 3, 98, 9, 76, 45, 4]
# n = []
# def check(a):
# 	new = []
# 	for i in range(len(a)):
# 		x = [int(j) for j in str(a[i])]
# 		new.append(x)
# 	p= max(new, key=lambda x: x)
	
# 	print p[0]

# check(a)

# from fractions import Fraction
# x = sorted(a, key=lambda n: Fraction(n, 10**len(str(n))-1), reverse=True)
# print x

#a = ["1", "34", "3", "98", "9", "76", "45", "4"]
a = ['1','34','3','98','9','76']
for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if a[i]+a[j] < a[j]+a[i]:
            a[i], a[j] = a[j], a[i]  
print ''.join(a)