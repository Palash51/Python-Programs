class Que:

	def __init__(self):
		self.data = []
	def isEmppty(self):
		return self.data == []


	def enque(self,new_data):
		self.data.insert(0,new_data)

	def deque(self):
		return self.data.pop()

	def display(self):

		return self.data


q = Que()
q.enque(1)
q.enque(2)
print q.deque()
print q.display()
