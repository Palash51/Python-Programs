from collections import Counter as C

para = open('file.txt').read()


def count_k_most_words(para,k):
	new = para.split()
	count = C(new)
	
	res = reversed(count.most_common(k))
	for x in res:
		print(x[0], ':' ,x[1])


k = int(input())
para = open('file.txt').read()
(count_k_most_words(para,k))