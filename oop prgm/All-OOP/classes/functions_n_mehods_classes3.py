## tutorial 3 --
# --method-- methods is a block of code which is part of a class, 
# --- methosd is always associated with class and object instance,


# --function-- outside a class is called as function, independent by itself



class Point:
	
	def assign(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z

	def print_point(self):
		print(self.x,self.y,self.z)

def fun1(a, b):
	return a+b


print(fun1(1,2))


p1 = Point()
p1.assign(1,2,3)
#p1.print_point()


p2 = Point()
p2.assign(4,-2,5)
#p2.print_point()