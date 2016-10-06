class Sta:

	def __init__(self): 
		self.data = []

	def isEmpty(self):
		return self.data == []
			

	def push(self,new_data):
		return self.data.append(new_data)
		#print new


	def pop(self):
		return self.data.pop()

	
	def display(self):
		return [x for x in reversed(self.data)]


		


s = Sta()
s.push(1)
# s.push(2)
# s.push(3)
print s.isEmpty()
print s.display()
# print s.pop()
# print s.pop()



# from collections import deque
# a = deque(a)
# a.rotate(2)
# a.insert(0,a.pop()) #pop out element from last and insert at beg
