class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.size = k
        self.front = -1
        self.rear = -1
        self.A = [None] * self.size

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        elif self.isEmpty():
            self.front = self.rear = 0
        else:
            self.front = (self.front - 1) % self.size 
        self.A[self.front] = value
        return True 
        

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        elif self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.A[self.rear] = value
        return True 

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        elif self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return True

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        elif self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.rear = (self.rear - 1) % self.size
        return True

    def getFront(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.A[self.front]

    def getRear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.A[self.rear]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.front == self.rear == -1

    def isFull(self):
        """
        :rtype: bool
        """
        return (self.rear + 1) % self.size == self.front


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()