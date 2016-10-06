def median(item):
    sort_item = sorted(item)
    #print sort_item
    item_len = len(sort_item)
    #print item_len
    #odd list or even list
    median = 0
    if item_len%2 == 0:
        #item_even = sort_list
        a = item_len / 2
        #print a
        #print sort_item[a]
        b = a - 1
        #print b
        #print sort_item[b]
        median = (sort_item[a] + sort_item[b]) / 2.0
        return median
    else:
        median = item_len / 2
        #print median
        return sort_item[median]

print median([4,5,5,4])        