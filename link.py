class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

mylist = UnorderedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))

mylist.add(100)
print(mylist.search(100))
print(mylist.size())
print mylist.data
mylist.remove(54)
print(mylist.size())
mylist.remove(93)
print(mylist.size())
mylist.remove(31)
print(mylist.size())
print(mylist.search(93))

# class node:
#     def __init__(self):
#         self.data = None 
#         self.next = None 

# class linked_list:
#     def __init__(self):
#         self.cur_node = None
#        #self.root = None
#         #self.head = None
#     def add_node(self, data):
#         if root == None:
#             new_node = node()
#             new_node.data = data
#             new_node.next = None
#             root = new_node
#             head = new_node
#         else:
#             new_next = node()
#             new_next.data=data
#             new_next.next = None
#             head.next=new_next
#         # new_node = node() 
#         # new_node.data = data
#         # new_node.next = self.cur_node 
#         # self.cur_node = new_node 
#         # print new_node.data
#     def display(self):
#         if root==None:
#             print "list is empty"
#         else:
#             current = self.root
#             while (current!=None):
#                 print"hola"
#                 print current.data
#                 current=current.next
#     # def list_print(self):
#     #      x = self.cur_node 
#     #      while x:
#     #          print x.data
#     #          x = x.next


# root = None
# head = None
# ll = linked_list()
# ll.add_node(10)
# ll.add_node(5)
# ll.add_node(8)
# ll.add_node(12)
# ll.display()
# #ll.list_print()