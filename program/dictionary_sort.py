def sortByValue(dictionary):
    tmp = []
    for key,value in dictionary.items():
        tmp.append((value,key))
    tmp.sort()
    return tmp
def sortByKey(dictionary):
    tmp = []
    for key,value in dictionary.items():
        tmp.append((key,value))
    tmp.sort()
    return tmp

#test the sorts.
dictionary = {"c":1, "b":2, "a":3}


print (sortByValue(dictionary))
print (sortByKey(dictionary))
