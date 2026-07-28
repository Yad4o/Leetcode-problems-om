class RecentCounter(object):

    def __init__(self):
        self.A =[]
        self.B = 0
    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.A.append(t)
        while self.A[self.B] < t -3000:
            self.B += 1
        return len(self.A) - self.B


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)