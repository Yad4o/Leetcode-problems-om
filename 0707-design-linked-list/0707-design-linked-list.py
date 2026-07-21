class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0:
            return -1
        a = 0
        temp = self.head 
        while temp is not None:
            if a == index:
                return temp.val
            temp = temp.next
            a += 1
        return -1
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        A = Node(val)
        A.next = self.head
        self.head = A

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        A = Node(val)
        if self.head is None:
            self.head = A
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = A

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0:
            return 
        if index == 0:
            self.addAtHead(val)
            return
        temp = self.head
        a = 0
        while temp is not None and a < index -1:
            temp = temp.next
            a += 1
        if temp is None:
            return
        A = Node(val)
        A.next = temp.next
        temp.next = A


    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if self.head is None or index < 0:
            return
        if index == 0:
            self.head = self.head.next
            return
        a = 0
        temp = self.head
        while temp is not None and a < index -1:
            temp = temp.next
            a += 1
        if temp is None or temp.next is None:
            return
        temp.next = temp.next.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)