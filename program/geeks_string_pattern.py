'''a = "GeeksforGeeks"
b = {'g' : 'X', 'e': 'Y'}

for p,q in b.iteritems():
    a = a.replace(p,q)

print a
'''
'''
d={'Ge':'X'}
c = ''.join(d[s] for s in "GeeksforGeeks" if s in d.values())
print c
'''


text = raw_input()
pat = raw_input()
#text = "GeeksforGeeks"

p = text.replace(pat,'X')
print p

'''
w_dic = {"Geeks": "X"}
c_dic = {'E':'3', 'e':'3', 'o':'0'}
text = replace(text, w_dic)
#text = replace_all(text, c_dic)
print text
'''






'''
def compare(str1,pattern):
    for i in range(0,pattern[i]):
        if str1[i] != pattern[i]:
            return False
    return True



def repl(str1,pattern):
    lght = len(pattern)

    if lght == 0:
        return

    i = 0
    j = 0
    while(str1[j]):
        count = 0
        while(compare(str1+str(j), pattern)):
            j = j + lgth
            count = count + 1

        if count > 0:
            str1[i+1] = 'X'

        if str1[j]:
            str1[i+1] = str1[j+1]


    str1[i] = '\0'


str1 = "GeeksforGeeks"
pattern = "Geeks"
print repl(str1,pattern)
'''
