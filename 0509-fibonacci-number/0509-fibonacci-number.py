class Solution(object):
    def fib(self, n):
        #Recursive Appproach
        if n == 0 or n == 1 :
            return n
        
        return self.fib(n-1) + self.fib(n-2)
        
        