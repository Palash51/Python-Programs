def median(alist):
	alist = alist.sort()
	len1 = len(alist)
	if len1 % 2 != 0:
		midl = (len1 /2)
		res = alist[midl]
	else:
		odd = (len1 / 2) -1
		ev = (len1 / 2)
		res = float(alist[odd] + alist[ev]) / float(2)

	return res

#num = []
#n = raw_input()
#num.extend([int(i) for i in n.split(" ")])
print median([1, 2, 4, 3])