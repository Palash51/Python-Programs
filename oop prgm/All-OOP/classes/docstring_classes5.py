## tutorial -- 5
# --docstring--
# we can access docstring of module(file)

'This is a class demo'

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


p1 = Point(1,2,3) #defining as well as instantiating object
# p1.print_point()


p2 = Point(4,8,9)
# p2.print_point()

print(__doc__)  ## entire module (file)
print(p1.__doc__) ## docstring of a class
print(p1.print_point.__doc__) ## docstring of methods
print(p1.__init__.__doc__) ## docstring of initializer method


# print(help(p1)) ## another way of printing doctstring





