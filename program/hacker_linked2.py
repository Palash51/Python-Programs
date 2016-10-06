class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):

        self.head = None


    #def insertAfter(self,prev_node,new_node)

    def append(self,new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while(last.next):
            last = last.next

        last.next = new_node
        #return new_node

    def printList(self):
        temp = self.head
        while(temp):
            for i in str(temp.data):
                print i
            temp = temp.next


l = LinkedList()
lst = map(int,raw_input().split())

t = input()
for i in range(t):
    num = input()
    for k in range(num):
        lst = map(int,raw_input().split())
    print lst
        
l.append(lst)
l.printList()
        
