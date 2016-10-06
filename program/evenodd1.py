num = input()
new = []
#i = 0

if num % 2 == 0:
    i = 0
    while(len(new) < num):
        new.append(i)
        i = i + 2

else:
    i = 1
    while(len(new) < num):
        new.append(i)
        i = i + 2
    
    
print new
