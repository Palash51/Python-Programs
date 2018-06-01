## tutorial -- handling-exception by types
## different blocks 
def main():

	try:
		a = 1
		b = 0
		c = a/b
		print("ayaaaa")
	except ZeroDivisionError as err:
		print("Error :{0}".format(err))
		print("Running the code for division by zero")
	except TypeError as err:
		print("Error :{0}".format(err))
		print("Running the code for type error")
	except Exception as err:
		print("Error :{0}".format(err))
		print("Running the code for general errors")


	print("Debug: yha to aaya h bhai")

if __name__ == '__main__':
	main()
