class MinStack(object):

    def __init__(self):
        self.A = []
        self.B = []

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        if not self.B or value <= self.B[-1]:
            self.B.append(value)
        self.A.append(value)

    def pop(self):
        """
        :rtype: None
        """
        if self.A[-1] == self.B[-1]:
            self.B.pop()
        self.A.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.A[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.B[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()