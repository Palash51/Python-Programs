class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkList:

    def __init__(self):
        self.head = None

    def push(self,newdata):
        newnode = Node(newdata)
        newnode.next = self.head
        self.head = newnode
        print newdata


l = LinkList()
l.push(1)
l.push(2)
l.push(3)
        
