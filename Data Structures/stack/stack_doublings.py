class Stack(object):

	def __init__(self,limit = 5):
		self.items = limit*[None]
		self.limit = limit

	def isEmpty(self):
		return self.items == []

	def push(self,item):
		if len(self.items) >= self.limit :
			self.resize()

		self.items.append(item)
		#print "Stack after push", self.items

	def pop(self):
		if len(self.items) <= 0:
			print "Stack Underflow"
			return 0

		else:
			return self.items.pop()

	def peek(self):
		if len(self.items) <= 0:
			print "Stack overflow"

		else:
			return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)

	def resize(self):
		newStk = list(self.items)
		self.limit = 2*self.limit
		self.items = newStk

	def display(self):
		print self.items


s = Stack(5)
s.push('1')
s.push('21')
s.push('14')
s.push('11')
s.push('31')
s.push('14')
s.push('15')
s.push('19')
#s.push('3')
s.push('99')
s.push('9')
print s.peek()
s.display()



