class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self,newdata):
		self.data = newdata

	def setNext(self,newnext):
		self.next = newnext

class LinkedLIst:
	def __init__(self):
		self.head = None

	def isEmpty(self):
		print self.head == None


	def add(self,item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp
		print item

    def reve(self,newhead):
    	self.head = newhead
        self.prev = None
        self.next = None
        while self.head: 
        	self.next = self.head.next
            self.head = prev
            self.prev = self.head
            self.head = self.next


        return self.prev


mylist = LinkedLIst()
mylist.add(31)
mylist.add(10)
mylist.add(2)
mylist.add(3)