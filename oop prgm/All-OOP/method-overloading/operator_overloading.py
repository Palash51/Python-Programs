## tutorial -- operator overloading
## assignig extra work to operator
## making operators to work for the objects to user defined classes


class Point:

	def __init__(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z

	def __str__(self):
		return ("({0},{1},{2})".format(self.x,self.y,self.z))

	def __add__(self, other):
		"""to overload + operator we have to use __add__"""
		self.x = self.x + other.x   # self.x = str(self.x) + str(other.x)
		self.y = self.y + other.y
		self.z = self.z + other.z
		return Point(self.x, self.y, self.z)

def main():
	p1 = Point(1,2,3)
	p2 = Point(4,5,6)
	print(p1)
	print(p2)
	print(p1+p2)

if __name__ == '__main__':
	main()
