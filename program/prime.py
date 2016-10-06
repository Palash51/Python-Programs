'''
n = input()
lst = list(map(int,raw_input().split()))
#print lst
print lst.sort()
'''
'''
for i in range(len(lst)-1):
    for j in range(i+1,len(lst)-1):
        if lst[j] == lst[i]:
            lst.remove(lst[j])

print lst
'''
t = 3, 5, 7, 2, 2, 5, 7, 7
s = []
for i in t:
       if i not in s:
          s.append(i)

print s
