## tutorial -- encapsulation

#### no access modifier in python

### __var is treated as private, not accessible from outside but it is possible,
### to access it, we need to do name mangling (A()._A__var)

class A:

	def __init__(self):
		self.a = "Public"
		self._b= "Internal use only" # convention.. generally can not used outside
		self.__c = "name mangling in object"



def main():
	obj = A()
	print(obj.a)
	print(obj._b)
	# print(obj.__c)
	print(obj._A__c)


if __name__ == '__main__':
	main()