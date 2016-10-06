#432456

num = int(raw_input())
new = []
output = []
seen = set()
rem = 0
temp = num

while(temp > 0):
    rem = temp % 10
    temp = temp / 10
    new.append(rem)
    for val in new:
        if val not in seen:
            output.append(val)
            seen.add(val)
print output
        
    
