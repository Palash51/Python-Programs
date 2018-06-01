## tutorial -- hybrid ineritance or diamnod problem
## super() will remove redundancy (diamnod of dead problem)

class A:
	
	def m(self):
		print("m() from class A")

class B(A):
	
	def m(self):
		print("m() from class B")
		super().m()

class C(A):
	
	def m(self):
		print("m() from class C")
		super().m()


class D(B, C):
	
	def m(self):
		print("m() from D")
		super().m()
		# B.m(self)
		# C.m(self)
		# A.m(self)

def main():
	obj1 = D()
	obj1.m()



if __name__ == '__main__':
	main()





##################################


class A:
	
	def m(self):
		print("m() from class A")

class B(A):
	
	def m(self):
		print("m() from class B")

class C(A):
	
	def m(self):
		print("m() from class C")


class D(B, C):
	
	def m(self):
		print("m() from D")
		B.m(self)
		C.m(self)
		A.m(self)

def main():
	obj1 = D()
	#obj1.m()



if __name__ == '__main__':
	main()
