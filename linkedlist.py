class Node:
	def __init__(self):
		self.data = None
		self.next = None

	def setData(self,data):
		self.data = data

	def getData(self):
		return self.data

	def setNext(self,next):
		self.next = next

	def getNext(self):
		return self.next

	def hasNext(self):
		return self.next != None

class Linkedlist:
	def __init__(self):
		self.head = None
	def listlenght(self):
		curr = self.head
		count = 0

		while curr != None:
			count = count + 1
			curr = curr.getNext()
			
		return count


l = Node()
l.setData(1)
l.setData(2)
l.setData(3)
s = 
print l.listlenght()