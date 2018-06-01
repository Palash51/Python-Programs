## tutorial 2 --
# --self-- reference to the obj which is invoking particular methods and 
# -- refers to the instance which is going to use all the variables and methods


class Point:
	
	def assign(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z

	def print_point(self):
		print(self.x,self.y,self.z)


p1 = Point()
# p1.x = 2
# p1.y = 3
# p1.z = 5

p1.assign(1,2,3)
p1.print_point()
# print(p1.assign(p1.x,p1.y,p1.z))

p2 = Point()
p2.assign(4,-2,5)
p2.print_point()