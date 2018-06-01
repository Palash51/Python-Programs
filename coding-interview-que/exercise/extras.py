class Expense(object):
	
	def __init__(self, initial_amt):
		self.initial_amt = initial_amt
		# self.new_amt = new_amt

	def spent(self, people_list, rup):

		new_list = []
		for p in people_list:
			new_total = initial_amt[p] - rup
			initial_amt[p] = new_total
			print("\n", p + " has spent", rup, " new amout is", new_total)
			new_list.append(p)

		# for p in initial_amt:
		# 	if p not in new_list:
		# 		print("\n", p + " did not spend anything")
			


	def borrowed(self, people_list, rup, lender):

		new_list = []
		for p in people_list:
			new_total = initial_amt[lender] - rup
			new_sum = initial_amt[p] + rup
			initial_amt[p] = new_sum
			initial_amt[lender] = new_total
			print("\n", p + " has borrowed ", rup, " from ", lender)
			new_list.append(p)
		print("\n", lender + " has lended", rup, " to ", ' & '.join([str(item) for item in people_list]))


		for p in initial_amt:
			if p not in new_list and p != lender:
				print("\n", p + " did not borrow anything")

		#print("Updated amount for each person", initial_amt)  


# print("Initial Balance of each person \n")
initial_amt = {'A': 1000,
		'B': 700,
		'C': 300,
		'D': 500}
# print(initial_amt)

# new_amt = {'A':0, 'B':0, 'C':0, 'D':0}

e = Expense(initial_amt)

# print("\nEnter your choice 1 for spending, 2 for borrowing")
#choice = int(input())

#if choice == 1:
	#print("Enter your spent amount details")
	# people_list = [x for x in input().split()]
	# spent_amount = int(input())
people_list = ['A', 'B']
spent_amount = 200
e.spent(people_list,spent_amount)

#elif choice == 2:
	# print("Enter your borrowed amount details")
	# people_list = [x for x in input().split()]
	# spent_amount = int(input())
	# print("borrowed from whom")
	# lender = input()
people_list = ['A', 'B']
spent_amount = 200
lender = 'D'
e.borrowed(people_list,spent_amount,lender)


# else:
# 	print("Invalid choice")



####test cases ####

#list of people who has spent -->     people_list = ['A', 'B', 'D']
# spent amount                -->     sprnt_amout = 200

#list of people who has borrowed -->     people_list = ['A', 'C']
# amount borrowed                -->     borrowed_amount = 100
# lender who gives money         -->     lender = 'D'

########################