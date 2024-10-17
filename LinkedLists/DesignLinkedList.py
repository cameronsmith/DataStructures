class Node(object):
    def  __init__(self, val = None, next = None):
        self.val = val
        self.next = next
        
class MyLinkedList(object):
    def __init__(self):
        self.head = None
        

    def get(self, index):
        if self.head is None:
            return -1
        
        cur = self.head
        cur_position = 0
        
        while cur is not None and cur_position < index:
            cur_position += 1
            cur = cur.next
            
        if cur_position == index and cur is not None:
            return cur.val
        
        return -1

    def addAtHead(self, val):
        if self.head is None:
            self.head = Node(val)
            return
        
        node = Node(val, self.head)
        self.head = node
        

    def addAtTail(self, val):
        if self.head is None:
            self.head = Node(val)
            return
        
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            
        cur.next = Node(val)
        

    def addAtIndex(self, index, val):
        if index == 0:
            self.addAtHead(val)
            return
        
        cur_position = 0
        cur = self.head
        while cur_position < (index - 1) and cur is not None:
            cur_position += 1
            cur = cur.next
            
        if cur is not None and cur_position < index:
            new = Node(val, cur.next)
            cur.next = new
            return
        

    def deleteAtIndex(self, index):
        if self.head is None:
            return
        
        if index == 0:
            self.head = self.head.next
            return
        
        cur_position = 0
        cur = self.head
        while cur_position < (index - 1) and cur is not None:
            cur_position += 1
            cur = cur.next
            
        if cur is not None and cur.next is not None:
            next = cur.next.next
            cur.next = next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)