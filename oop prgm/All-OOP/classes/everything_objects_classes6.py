## tutorial -- 6
## --- everything in python is an object

class Point:
	"""Class Point for cordinates"""

	def __init__(self,x,y,z):
		"""initializer method for class"""
		self.x = x
		self.y = y
		self.z = z

	def print_point(self):
		"""it will print the cordinates of point"""
		print(self.x,self.y,self.z)


p1 = Point(1,2,3) 
# print(type(p1))


p2 = Point(4,8,9)
# print(type(p2))

print(type(p1.print_point))

# a = 2
# b = "hii"
# c = 2.5
# print(type(a),type(b), type(c))