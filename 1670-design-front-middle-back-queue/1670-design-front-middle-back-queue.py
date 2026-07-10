class FrontMiddleBackQueue(object):

    def __init__(self):
        self.A = deque()
        self.B = deque()

    def pushFront(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.A.appendleft(val)

    def pushMiddle(self, val):
        """
        :type val: int
        :rtype: None
        """
        mid = len(self.A) // 2
        for _ in range(0, mid):
            self.B.appendleft(self.A.popleft())
        self.A.appendleft(val)
        for _ in range(0, len(self.B)):
            self.A.appendleft(self.B.popleft())

    def pushBack(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.A.append(val)

    def popFront(self):
        """
        :rtype: int
        """
        if self.A:
            return self.A.popleft()
        return -1
        

    def popMiddle(self):
        """
        :rtype: int
        """
        if not self.A:
            return -1
        mid = (len(self.A) - 1) // 2
        for _ in range(0, mid):
            self.B.appendleft(self.A.popleft())
        a = self.A.popleft()
        for _ in range(0, len(self.B)):
            self.A.appendleft(self.B.popleft())
        return a

    def popBack(self):
        """
        :rtype: int
        """
        if self.A:
            return self.A.pop()
        return -1


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()