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



class LinkedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        print(self.head == None)

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        print(item)

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        print(count)

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        print(found)


mylist = LinkedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)
mylist.size()
mylist.search(18)
mylist.isEmpty()