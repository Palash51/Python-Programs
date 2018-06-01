## tutorial -- raise ecxeption

def main():

	try:
		a = 1
		b = 0
		if b == 0:
			raise Exception("an ecxeption has been raised")
		c = a/b
	except Exception as err:
		print("Error :{0}".format(err))
		
	else:
		print("No exception found")
		

	# print("Debug: yha to aaya h bhai")

if __name__ == '__main__':
	main()