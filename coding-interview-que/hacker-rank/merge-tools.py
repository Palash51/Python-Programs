def merge_the_tools(string, k):
	new = []
	final = []
	l = 0 
	while(l<len(string)):
		new.append(string[l])
		l = l + 1
		if len(new) == k:
			final.append(''.join(sorted(set(new), key=new.index)))
			new = []

	for item in final:
		print(item)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)