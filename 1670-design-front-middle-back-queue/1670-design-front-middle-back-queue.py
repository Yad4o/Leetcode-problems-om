class FrontMiddleBackQueue(object):
    
    def __init__(self):
        self.A = deque()
        self.B = deque()

    def pushFront(self, val):
        self.A.appendleft(val)

    def pushMiddle(self, val):
        mid = len(self.A) // 2
        for _ in range(0, mid):
            self.B.appendleft(self.A.popleft())
        self.A.appendleft(val)
        for _ in range(0, len(self.B)):
            self.A.appendleft(self.B.popleft())

    def pushBack(self, val):
        self.A.append(val)

    def popFront(self):
        if self.A:
            return self.A.popleft()
        return -1

    def popMiddle(self):
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
        if self.A:
            return self.A.pop()
        return -1