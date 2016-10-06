"""
 Print elements of a linked list on console
 head input could be None as well for empty list
 Node is
 defined as
 """

### Print ELEMENT in LL ###
'''
class Node(object):
 
   def __init__(self, data):
       self.data = data
       self.next = None
       #new = []
 
class LinkedList:
    
    def __init__(self):
        self.head = None
        #new = []
        
    def push(self,new_data):
        new = []
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        #print new_data
        #for i in new_data:
         #   print new_data

    def printList(self):
       new = []
       temp = self.head
       while (temp):
            new.append(temp.data)
            temp = temp.next
       #print new
       for k in new:
           #print k
           for p in k:
               print p
            
        

    
        
         
l = LinkedList()
t = input()
for i in range(t):
    num = input()
    for x in range(num):
        inp = list(map(int,raw_input().split()))
l.push(inp)
l.printList()
#l.push(1)
#l.push(2)
#l.push(3)
#l.printlist()
'''




















