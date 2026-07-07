class MyStack(object):

    def __init__(self):
        self.A = []
        

    def push(self, x):
        self.A.append(x)

    def pop(self):
        if not self.A:
            return 
        return self.A.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.A[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.A) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()