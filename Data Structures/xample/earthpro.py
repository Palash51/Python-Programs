def good_string(item):
    list_item = list(item)
    new_list = ['']
    j = 0
     
    for i in list_item:
    	if i != new_list[j]:
    		new_list.append(i)
    		j += 1
    return "".join(new_list)		

print good_string('aab')