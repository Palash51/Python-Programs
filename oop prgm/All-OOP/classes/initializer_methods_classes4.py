## tutorial --4
# --initializer-- 
# --- it will called as soon as the object of classs is being created



class Point:

	def __init__(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z

	def print_point(self):
		print(self.x,self.y,self.z)


p1 = Point(1,2,3) #defining as well as instantiating object
p1.print_point()


p2 = Point(4,8,9)
p2.print_point()