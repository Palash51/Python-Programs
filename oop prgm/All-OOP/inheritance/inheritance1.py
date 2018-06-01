## tutorial -- inheritance

class Person:

	def __init__(self,a,b,c):
		self.a = a
		self.b = b
		self.c = c
	
	def method1(self):
		print(self.a, self.b, self.c)


class Employee(Person):
	pass


def main():
	obj1 = Person(1,2,3)
	obj2 = Employee(4,5,6)
	
	obj1.method1()
	obj2.method1()


if __name__ == "__main__":
	main()