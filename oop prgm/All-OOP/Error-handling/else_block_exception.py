## tutorial -- else in ecxeption
import sys

def main():

	try:
		a = 1
		b = 1
		c = a/b
	except ZeroDivisionError as err:
		print("Error :{0}".format(err))
		print("Running the code for division by zero")
		sys.exit(1)
	except TypeError as err:
		print("Error :{0}".format(err))
		print("Running the code for type error")
		sys.exit(1)
	except Exception as err:
		print("Error :{0}".format(err))
		print("Running the code for general errors")
		sys.exit(1)
	else:
		print("No exception found")
		sys.exit(0)


	# print("Debug: yha to aaya h bhai")

if __name__ == '__main__':
	main()