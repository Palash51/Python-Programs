

# a = [[1,0,1],[1,1,1],[1,0,0]]

n = int(input().strip())
a = [[0]*n for _ in range(n)]
for i in range(n):
    a[i] = [int(j) for j in input().strip().split(" ")]



def get_rows(grid):
    return [[c for c in r] for r in grid]

def get_cols(grid):
    return zip(*grid)


def get_backward_diagonals(grid):
	print(grid)
	b = [None] * (len(grid) - 1)
	grid = [b[i:] + r + b[:i] for i, r in enumerate(get_rows(grid))]
	return [[c for c in r if not c is None] for r in get_cols(grid)]

def get_forward_diagonals(grid):
	print(grid)
	b = [None] * (len(grid) - 1)
	grid = [b[:i] + r + b[i:] for i, r in enumerate(get_rows(grid))]
	return [([c for c in r if not c is None]) for r in get_cols(grid)]

print(get_forward_diagonals(a))