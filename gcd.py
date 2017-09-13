def GCD(a,b):
	""" The Euclidean Algorithm """
    a = abs(a)
    b = abs(b)
    while a:
        a, b = b%a, a
    return b
        
        
def GCD_List(list):
	""" Finds the GCD of numbers in a list.
	Input: List of numbers you want to find the GCD of
		E.g. [8, 24, 12]
	Returns: GCD of all numbers
	"""
	return reduce(GCD, list)

print([12,16])
