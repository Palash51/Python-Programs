## tutorial -- multiple inheritance

## method resolution order

class A:
	
	def m(self):
		print("m() from class A")

class B:
	
	def m(self):
		print("m() from class B")

class C(B, A):
	def m(self):
		print("m() from class C")


def main():
	obj1 = C()
	obj1.m()



if __name__ == '__main__':
	main()






##############################

# class A:
# 	pass

# class B:
# 	pass

# class C(A, B):
# 	pass


# def main():
# 	obj1 = C()



# if __name__ == '__main__':
# 	main()