class Node:
	def __init__(self,data):
		self.data = data
		self.next = None


class Stack:
	def __init__(self,data = None):
		self.head = None
		#if data is not None:
		#	for data in data:
		#		self.push(data)

	def push(self,data):
		temp = Node(data)
		#temp.data = data
		temp.next = self.head
		self.head = temp
		print data


	def pop(self):
		if self.head is None:
			print "empty"

		temp = self.head.data
		self.head = self.head.next
		return temp

	def peek(self):
		if self.head is None:
			print "empty stack"

		return self.head.data

#orl = [1,2,3,4]
ours = Stack()
ours.push(1)
ours.push(2)
print ours.pop()
print ours.peek()
