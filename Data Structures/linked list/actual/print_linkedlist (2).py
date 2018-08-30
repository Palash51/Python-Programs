
class Node(object):
   def __init__(self, data):
       self.data = data
       self.next = None


class LinkedList:

    def __init__(self):
        self.head = None  
    
    def push(self,new_data):
        new = []
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node 
    
    def printList(self):
       new = []
       temp = self.head
       while (temp):
            new.append(temp.data)
            temp = temp.next
       for k in reversed(new):
            print(k)

l = LinkedList()
t = input()
for i in range(t):
    num = input()
    if num == 0:
      i = i + 1
    else:
      inp = list(map(int,raw_input().split()))
      for item in inp:
        l.push(item)
l.printList()
