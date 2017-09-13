class Node :
	def __init__( self, data ) :
		self.data = data
		self.next = None
		#self.prev = None

class LinkedList :
	def __init__( self ) :
		self.head = None		

	def add( self, data ) :
		node = Node( data )
		if self.head == None :	
			self.head = node
		else :
			node.next = self.head
			#node.next.prev = node						
			self.head = node			

	# def search( self, k ) :
	# 	p = self.head
	# 	if p != None :
	# 		while p.next != None :
	# 			if ( p.data == k ) :
	# 				return p				
	# 			p = p.next
	# 		if ( p.data == k ) :
	# 			return p
	# 	return None

	#def remove( self, p ) :
		#tmp = p.prev
		#p.prev.next = p.next
		#p.prev = tmp		

	def __str__( self ) :
		s = ""
		p = self.head
		if p != None :		
			while p.next != None :
				s += p.data
				p = p.next
			s += p.data
		return s

# example code
l = LinkedList()

(l.add(1)
l.add(2)
l.add(3)

print l
#l.remove( l.search( 'b' ) )
print
print l
# class Node:

# 	def __init__(self):
# 		self.data = None
# 		self.next = None

# 	def setData(self,data):
# 		self.data = data

# 	def getData(self):
# 		return self.data

# 	def setNext(self,next):
# 		self.next = next

# 	def getNext(self):
# 		return self.next
	
# 	def hasNext(self):
# 		return self.next != None


# 	def insert_beg(self,data):
# 		new_node = Node()
# 		new_node.setData(data)
# 		#self.head = new_node
# 		new_node.setNext(self.head)
# 		#self.head = new_node
# 	#	self.length += 1

# l = Node()
# l.insert_beg(1)
# l.insert_beg(2)














# class Node:

# 	def __init__(self):
# 		self.data = None
# 		self.next = None

# class Linkedlist:

# 	def __init__(self):
# 		self.head = None

# 	def insert(self,data):
# 		new_node = Node()
# 		new_node.data = data
# 		new_node.next = self.head
# 		self.head = new_node

# #		
# 	def display(self):
# 		current = self.head
# 		while current:
# 			print current.data
# 			current=current.next
			

# l = Linkedlist()
# l.insert(1)
# l.insert(2)
# l.insert(3)

# l.display()
