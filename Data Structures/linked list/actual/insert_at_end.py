class Node(object):
   def __init__(self, data):
       self.data = data
       self.next = None
class LinkedList:
    def __init__(self):
        self.head = None  


    def Insert(head, data):
      node_data = Node(data)
      current = head
      if current is None:
          head = node_data
          node_data.next = None
          return head
      if current.next is None:
          current.next = node_data
          node_data.next = None
          return head
      while current.next is not None:
          current = current.next
      current.next = node_data
      node_data.next = None
      return head
    





    # def Insert(self, new_data):
    #     new_node = Node(new_data)
 
    #     if self.head is None:
    #         self.head = new_node
            
    #     else:
    #       last = self.head
    #       while (last.next):
    #          last = last.next
    #          last.next =  new_node


    #     new = []
    #     temp = self.head
    #     while (temp):
    #         new.append(temp.data)
    #         temp = temp.next
        
    #     #if len(new) != 0:
    #     for ele in new:
    #       print ele


new1 = []
l = LinkedList()
#t = input()
#for i in range(t):
num = raw_input()
#new1.append(num)

#for x in new1:
l.Insert(num)




















