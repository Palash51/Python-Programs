class MyList:
    class ListNode:
        def __init__(self,value):
            self.value=value;
            self.next = None;

    def __init__(self):
        self.head=None;

    def append(self,value):
        node = self.ListNode(value)
        if (self.head==None):
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def reverse(self):
        cursor = self.head
        self.head = self.head.next
        cursor.next = None
        while self.head.next:
            temp = self.head.next
            self.head.next = cursor
            cursor = self.head
            self.head = temp
        self.head.next = cursor
'''
    def __str__(self):
        cursor = self.head
        string =  '( '
        while cursor:
            string += "{} ".format(cursor.value)
            cursor=cursor.next
        string += ')'
        return string


def iter1(start_node):
        curr = start_node
        prev = None
        next = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev





        
'''
list = MyList()
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)

print list
list.reverse()
print list
