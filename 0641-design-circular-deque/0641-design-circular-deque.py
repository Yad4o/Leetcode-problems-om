class MyCircularDeque(object):

    def __init__(self, k):
        self.size = k
        self.front = -1
        self.rear = -1
        self.A = [None] * self.size

    def insertFront(self, value):
        if self.isFull():
            return False
        elif self.isEmpty():
            self.front = 0
            self.rear = 0
        else:
            self.front = (self.front - 1) % self.size 
        self.A[self.front] = value
        return True 
        

    def insertLast(self, value):
        if self.isFull():
            return False
        elif self.isEmpty():
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.A[self.rear] = value
        return True 

    def deleteFront(self):
        if self.isEmpty():
            return False
        elif self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False
        elif self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.rear = (self.rear - 1) % self.size
        return True

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.A[self.front]

    def getRear(self):
        if self.isEmpty():
            return -1
        return self.A[self.rear]

    def isEmpty(self):
        return self.front == self.rear == -1

    def isFull(self):
        return (self.rear + 1) % self.size == self.front