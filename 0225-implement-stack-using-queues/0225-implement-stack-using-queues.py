class MyStack(object):

    def __init__(self):
        self.A = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.A.append(x)
        for _ in range (len(self.A) - 1):
            self.A.append(self.A.popleft())

    def pop(self):
        """
        :rtype: int
        """
        return self.A.popleft()

    def top(self):
        """
        :rtype: int
        """
        return self.A[0]

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