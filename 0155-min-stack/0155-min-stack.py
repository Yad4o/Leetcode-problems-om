class MinStack(object):

    def __init__(self):
        self.A = []
        self.minA = []
        

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.A.append(value)
        if not self.minA or value <= self.minA[-1]:
            self.minA.append(value)


    def pop(self):
        """
        :rtype: None
        """
        if self.A:
            if self.A[-1] == self.minA[-1]: 
                self.minA.pop()
            self.A.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.A:
            return self.A[-1]
        return None

    def getMin(self):
        """
        :rtype: int
        """
        if self.minA:
            return self.minA[-1]
        return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()