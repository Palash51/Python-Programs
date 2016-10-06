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
		print new_data
	    

	'''def insert_beg(self,data):
		new_node = Node()
		new_node.data = data

		if self.length == 0:
                    self.head = new_node
                else:
                    new_node.next = self.head
                    self.head = new_node
                self.length += 1

                print new_data


	def printList(self):
		temp = self.head
		while(temp):
			print temp.data,
			temp = temp.next

		
'''


llist = LinkedList()
llist.push(20)
llist.push(30)
llist.push(40)
llist.push(50)
llist.insert_beg(10)
#llist.printList()





