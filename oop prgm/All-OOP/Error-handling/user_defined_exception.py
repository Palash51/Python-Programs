## tutorial -- user defined ecxeption

## we are defining our exception
## Exception is built in class

class MyException(Exception):
	pass

class ValueSmallError(MyException):
	pass

class ValueLargeError(MyException):
	pass


def main():

	num = 10

	try:
		user_inp = int(input("please enter number"))

		if user_inp < num:
			raise ValueSmallError("please enter large value")
		if user_inp > num:
			raise ValueLargeError
		else:
			print("perfect")

	except ValueSmallError:
		print("Value is small")
	except ValueLargeError:
		print("Value is large")
	except Exception:
		print("unexpeted Error!!")


if __name__ == '__main__':
	main()