def print_rangoli(size):
	horizotal = size*2 - 2
	vertical = (size*2 - 1)*2 + 1
	a = [[0]*vertical for _ in range(horizotal)]
	matrix = [horizotal,vertical]
	print(matrix)



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)