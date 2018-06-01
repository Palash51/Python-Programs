## tutorial -- method overloading

### does not allow multiple method with same name
## but possible to achieve by passing different no of arguments


class A:

	def method01(self, i=None):

		if i is None:
			print("sequence 01")
		else:
			print("sequence 02")
			return 1


def main():
	obj = A()
	obj.method01()
	r = obj.method01(2)
	print(r)



if __name__ == '__main__':
	main()

