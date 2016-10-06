class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None

	def push(self,new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def insert_beg(self,n_data):
		new_node = Node(n_data)
		new_node.next = self.head
		self.head = new_node


	def printList(self):
		temp = self.head
		while(temp):
			print temp.data
			temp = temp.next


llist = LinkedList()
llist.push(10)
llist.push(20)
llist.push(30)
llist.push(40)
llist.push(50)





