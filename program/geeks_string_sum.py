'''
def str_sum(str1):

    #lst = list(str1)
    sum = 0
    new = []
    #count1 = [abcdefghijklmnopqrstuvwxyz]
    for i in str1:
        if i not in "abcdefghijklmnopqrstuvwxyz":
            new.append(i)

    print new

    


str_sum("abc1b2de3")
'''

str1 = "hjf35n4"
i = 0
sum = 0
temp = "0"
for j in range(0,15):
    temp[j] = '\0'
k = 0
for i,k in range(0,len(str1)):
    if isdigit(str1[i]):
        temp[k] = str1[i]
        k = k + 1

    else:
        sum = sum + str(temp)

    for j in range(0,15):
        temp[j] = ' '

print sum


'''
str = "abc 11 b2de23"
t = [int(s) for s in str.split() if s.isdigit()]
print t
'''

'''
def extract_nbr(input_str):
    if input_str is None or input_str == '':
        return 0

    out_number = []
    for ele in input_str:
        if ele.isdigit():
            #out_number += ele
            out_number.append(ele)
    return out_number    


print extract_nbr("hdhgi34gji5")
               
'''
'''
import re
str1 = "gfdgf45hkf6kf75ggg2"
print(re.findall('\d+', str1))
'''



'''

def digitsum3(x):
    total=0
    for letter in str(x):
        total+=ord(letter)-48
    return total 

print digitsum3("lsglg3df4")

'''









