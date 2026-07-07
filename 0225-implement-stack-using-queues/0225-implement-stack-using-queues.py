from collections import deque
class MyStack(object):

    def __init__(self):
        self.A = deque()
        

    def push(self, x):
        self.A.append(x)
        for _ in range(len(self.A)-1):
            self.A.append(self.A.popleft())

    def pop(self):
        if not self.A:
            return 
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