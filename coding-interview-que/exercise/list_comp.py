lst  =  [x ** 2  for x in range (1, 11)   if  x % 2 == 1] 
print(lst)


########## list comp. with condition ##########
print([x if x % 2 == 0 else "no" for x in range(10)])


######### nested list comp ############
data = [[1, 2], [3, 4], [5, 6]]
output = [element for each_list in data for element in each_list]
print(output)


####### dict comp ###########
print({x: x * x for x in (1, 2, 3, 4)})

d1 = {'w': 1, 'x': 1}
d2 = {'x': 2, 'y': 2, 'z': 2}
new = {k: v for d in [d1, d2] for k, v in d.items()}
print(new)