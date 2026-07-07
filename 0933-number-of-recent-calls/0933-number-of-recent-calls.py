class RecentCounter(object):

    def __init__(self):
        self.A = []
        self.count = 0
    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.A.append(t)
        while self.A[self.count] < t - 3000:
            self.count += 1
        return len(self.A) - self.count