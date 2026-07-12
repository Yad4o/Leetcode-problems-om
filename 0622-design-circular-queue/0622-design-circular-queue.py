class MyCircularQueue(object):

    def __init__(self, k):
        self.size = k 
        self.A = [None] * self.size 
        self.front = -1
        self.rear = -1

    def enQueue(self, value):
        if self.isFull():
            return False
        elif self.front == self.rear == -1:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % len(self.A)
        self.A[self.rear] = value
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        elif self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % len(self.A)
        return True

    def Front(self):
        if self.isEmpty():
            return -1
        return self.A[self.front]

    def Rear(self):
        if self.isEmpty():
            return -1
        return self.A[self.rear]

    def isEmpty(self):
        return self.front == self.rear == -1

    def isFull(self):
        return (self.rear + 1) % len(self.A) == self.front