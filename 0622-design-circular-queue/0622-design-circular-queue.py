class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.size = k
        self.A = [None] * self.size
        self.front = -1
        self.rear = -1

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.A[self.rear] = value
        return True
        

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        if self.front == self.rear:
            self.front = -1
            self.rear  = -1
        else:
            self.front = (self.front + 1) % self.size
        return True

    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.A[self.front]

    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.A[self.rear]
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.front == -1

    def isFull(self):
        """
        :rtype: bool
        """
        return (self.rear + 1) % self.size == self.front


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()