class Expense(object):
	
	def __init__(self, initial_amt):
		self.initial_amt = initial_amt
		# self.new_amt = new_amt

	# def spent(self, people_list, rup):

	# 	new_list = []
	# 	for p in people_list:
	# 		new_total = initial_amt[p] - rup
	# 		initial_amt[p] = new_total
	# 		# print("\n", p + " has spent", rup)
	# 		new_list.append(p)

		# for p in initial_amt:
		# 	if p not in new_list:
		# 		print("\n", p + " did not spend anything")
			


	def borrowed(self, people_list, rup, lender):

		new_list = []
		for p in people_list:
			spent = initial_amt[p] - rup # amount after spending rup
			new_total = initial_amt[lender] - rup # lender's amount
			new_sum = spent + rup # amount after borrowed amount
			initial_amt[p] = new_sum
			initial_amt[lender] = new_total
			print("\n", p + " has taken ", rup, " from ", lender)
			new_list.append(p)
		print("\n", lender + " has given ", rup, " to ", ' & '.join([str(item) for item in people_list]))


		for p in initial_amt:
			if p not in new_list and p != lender:
				print("\n", p + " did not borrow anything")

		#print("Updated amount for each person", initial_amt)  


# print("Initial Balance of each person \n")
initial_amt = {'A': 1000,
		'B': 1000,
		'C': 1000,
		'D': 1000}


e = Expense(initial_amt)


# people_list = ['A', 'B', 'D']
# spent_amount = 200
# e.spent(people_list,spent_amount)

people_list = ['B', 'C']
spent_amount = 200
lender = 'A'
e.borrowed(people_list,spent_amount,lender)



####test cases ####

#list of people who has spent -->     people_list = ['A', 'B', 'D']
# spent amount                -->     sprnt_amout = 200

#list of people who has borrowed -->     people_list = ['A', 'C']
# amount borrowed                -->     borrowed_amount = 100
# lender who gives money         -->     lender = 'D'

########################