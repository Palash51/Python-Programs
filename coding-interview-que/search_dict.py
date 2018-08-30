n = int(input())

d = dict(input().split() for x in range(n))

for i in d:
	s = input()
	if s in d:
		print(s+'='+d[s])
	else:
		print("Not found")

