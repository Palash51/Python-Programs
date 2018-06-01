def arrange_list(l):
	new = []
	i = 0
	while (i < len(l)/2):
		new.append(l[i])
		i = i + 1
	new.append(0)
	j = len(l) - 1
	while (j >= len(l)/2):
		new.append(l[j])
		j = j - 1
	print(new)
l = sorted([int(x) for x in input().split()])
arrange_list(l)



# def arrange_list(num):
# 	new = []
# 	new.append(num[0:int(len(num)/2)])
# 	new.append(num[int(len(num)/2):])
# 	print([j for i in new for j in i])	
# num = sorted([int(x) for x in input().split()])
# if len(num) % 2 == 0:
# 	arrange_list(num)
# else:
# 	num.insert(int(len(num)/2),0)
# 	arrange_list(num)


# def arrange_list(num):
# 	num = sorted(num)
# 	first_half = []
# 	second_half = []
# 	if len(num) % 2 == 0:
# 		first_half.append(num[0:int(len(num)/2)])
# 		second_half.append(num[int(len(num)/2):])
# 	else:
# 		first_half.append(num[0:int(len(num)/2)])
# 		first_half.append([0])
# 		second_half.append(num[int(len(num)/2):])
# 	new = first_half + second_half
# 	print([j for i in new for j in i])

# num = [int(x) for x in input().split()]
# arrange_list(num)


