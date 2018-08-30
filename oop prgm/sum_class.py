import functools

class Sum:
	""""""

	def __init__(self, lst):
		self.lst = lst

	def check_method(self, lst):
		""""""
		if len(lst) == 0:
			print("no ele")
			return None
		else:
			new = list(filter(lambda a :a != 0, lst))
			return new

	def sum_method(self):
		""""""
		ele = self.check_method(self.lst)
		total = functools.reduce(lambda a,b : a+b,lst)
		return total




lst = list(map(int, input().split()))

s = Sum(lst)
print(s.sum_method())