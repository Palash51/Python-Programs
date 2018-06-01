## tutorial -- finally ecxeption

def main():

	try:
		a = 1
		b = 0
		c = a/b
	except Exception as err:
		print("Error :{0}".format(err))		
	else:
		print("No exception found")
	finally:
		print("It will always execute")

	# print("Debug: yha to aaya h bhai")

if __name__ == '__main__':
	main()