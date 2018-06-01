l = [2, 11, 19, 35, 51, -4, 129, 151, 198, 7,500,35]
l = sorted(l)
#l= [-4]
d = {}
new = []
for i in l:
	if i < 0:
		no_range = (int(i/10))*10
		
		if i <= no_range and i >= (no_range-10):
			if ((no_range-10), "-",no_range) in d:
				d[(no_range-10), "-",no_range].append(i)
			else:
				d[(no_range-10), "-",no_range] = [i]

	else:
		no_range = (int(i/10))*10
		
		if i >= no_range and i <= (no_range+10):
			if (no_range, "-", (no_range+10)) in d:
				d[no_range, "-", (no_range+10)].append(i)
			else:
				d[no_range, "-", (no_range+10)] = [i]

print(d)



###################### iterator ##################




# def get_number(n):
# 	#n = it.__next__()
# 	r = (int(n/10))*10

# 	if n > r and n < r + 10:
# 		if (r, "-" ,r+10) in d1:
# 			d1[r, "-", r+10].append(n)
# 		else:
# 			d1[r, "-", r+10] = [n]



# l = [2, 11, 19, 35, 51, 4, 129, 152, 199, 7]
# d1 = {}
# it = iter(l)

# i = 0
# while i < len(l):
# 	print(get_number(it.__next__()))
# 	i = i + 1
	

#print(d1)


