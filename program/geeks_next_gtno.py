num = input()

lst = [int(l) for l in str(num)]
#print lst

for i in range(len(lst)-1,0,-1):
    if lst[i] < lst[i-1]:
        i = i - 1

    else:
        #print i
        temp = lst[i-1]
        lst[i-1] = lst[len(lst)-1]
        lst[len(lst)-1] = temp
        

print lst

