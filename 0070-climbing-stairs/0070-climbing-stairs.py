class Solution(object):
    def climbStairs(self, n):
        if n <= 1:
            return 1
        a = 1
        b = 1
        for i in range (2, n + 1):
            a , b = b , a + b
        return b
# class Solution(object):
#     def climbStairs(self, n):
#         if n == 1 or n == 0:
#             return 1
#         return self.climbStairs(n - 1) + self.climbStairs(n - 2)