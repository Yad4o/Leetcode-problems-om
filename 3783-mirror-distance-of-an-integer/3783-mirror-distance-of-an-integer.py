class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = n
        b = 0
        while n > 0:
            b = b * 10 + (n % 10)
            n = n // 10

        return abs(a - b)