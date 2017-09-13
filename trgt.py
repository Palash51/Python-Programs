targt = map(int,raw_input().split())
len_trgt = len(targt)
in_pos = [0]*len_trgt
final_count = 0

def reach_trgt(in_pos):
	print in_pos
	count = 0
	global final_count
	if cmp(in_pos,targt)!=0:
		if if_zero(in_pos):
			in_pos = [x+1 for x in in_pos]
			final_count +=1
			reach_trgt(in_pos)
		elif check_mul(in_pos):
			in_pos = [x*2 for x in in_pos]
			final_count+=1
			reach_trgt(in_pos)
		elif not check_mul(in_pos) and check_mul_oflow(in_pos):
			for i in range(len(in_pos)):
				if in_pos[i]*2<=targt[i]:
					in_pos[i]=in_pos[i]*2
					count+=1
			if count>=1:
				final_count+=1
				reach_trgt(in_pos)
		elif not check_mul_oflow(in_pos) and cmp(in_pos,targt)!=0 and check_add_oflow(in_pos) :
			for i in range(len(in_pos)):	
				if in_pos[i]+1<=targt[i]:
					in_pos[i]=in_pos[i]+1
					count+=1
			if count>=1:
				final_count+=1
				reach_trgt(in_pos)


	# else:
	# 	in_pos[i]+=1
	# 	final_count+=1
	# 	reach_trgt(in_pos)
	# else:
	# 	for i in range(len(in_pos)):
	# 		if in_pos[i]*2<targt[i]:
	# 			in_pos[i]*2
	# 			count+=1
	# 	if count>1:
	# 		final_count+=1
			
	# 	reach_trgt(in_pos)


def if_zero(x):
	return all(x[i]==0 for i in range(len(x)))

def check_mul(x):
	return all(x[i]*2<=targt[i] for i in range(len(x)))

def check_mul_oflow(x):
	flag = False
	count = 0
	for i in range(len(x)):
		if x[i]*2<=targt[i]:
			count+=1
			flag = True
	if count<len_trgt:
		return flag
	else:
		return flag == False

def check_add_oflow(x):
	flag = False
	for i in range(len(x)):
		if x[i]+1<=targt[i] and x[i]*2>targt[i]:
			flag=True
	return flag
reach_trgt(in_pos)
print final_count
