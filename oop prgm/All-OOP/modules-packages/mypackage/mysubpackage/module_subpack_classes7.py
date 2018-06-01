## tutorial --7
# --modularity--

# if we use __name__ method then we will sperate o1,o2 to execute from other module

class Class01:

	def __init__(self):
		print("created init method for class01")


class Class02:

	def __init__(self):
		print("created init for class02")


# if __name__ == "__main__":  ## checks whether its invoking directly or from other modules 
# 	o1 = Class01()
# 	o2 = Class02()

def main():
	"""all buisness logic here"""
	o1 = Class01()
	o2 = Class02()

if __name__ == "__main__":
	print("the module is being run directly")
	main()
else:
	print("the module is imported from 7")
