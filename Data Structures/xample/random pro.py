'''def Fun(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return Fun(n-1)+Fun(n-2)

t = int(raw_input())
for i in range(t):
	x = int(raw_input())
	print "%d %d" %(Fun(x-1), Fun(x))

t = int(raw_input())
for i in range(t+1):
	n = int(raw_input())
	arr = [0, 1]
	for i in range(2,n+1):
		arr[i] = arr[i-1] + arr[i-2]
		arr.append(arr[i])
	print "%d %d" %(arr[n-1], arr[n])'''

n = int(raw_input())
arr = raw_input()
num = []
num.extend(int(i) for i in arr.split(" "))
maxv = 0
for j in range(n):
	k = j
	while k > n:
	#for k in range(j, n):
		if j == k:
			j += 1
		else:
			numb = num[j]*num[k]
			if numb > maxv:
				maxv = numb
			j += 1
print maxv
