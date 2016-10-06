'''def remdup(a,n):
    k = 0
    a = list(a)
    print a
    for i in range(1,len(a)):
        if a[i-1] != a[i]:
            k = k + 1
            a[k] = a[i-1]

        else:
            while a[i-1] == a[i]:
                i = i + 1

    k = k + 1
    a[k] = a[i-1]
    #a[k] = '\0'

    if k!= n:
        remdup(a,k)

    else:
        return a

print remdup("geeksforgeek",12)
'''

def removeUtil(string, last_removed):
 
    
    if string[0] == string[1]:
        last_removed = ord(string[0])
        while len(string) > 1 and string[0] == string[1]:
            string = string[1:]
        string = string[1:]
 
        return removeUtil(string, last_removed)
 
    rem_str = removeUtil(string[1:], last_removed)
 
    if len(rem_str) != 0 and rem_str[0] == string[0]:
        last_removed = ord(string[0])
        return (rem_str[1:])
 
    if len(rem_str) == 0 and last_removed == ord(string[0]):
        return rem_str
 
    return ([string[0]] + rem_str)
 
def remove(string):
    last_removed = 0
    return toString(removeUtil(toList(string), last_removed))
 
# Utility functions
def toList(string):
    x = []
    for i in string:
        x.append(i)
    return x
 
def toString(x):
    return ''.join(x)
 
# Driver program
string1 = "geeksforgeeg"
print remove(string1)
