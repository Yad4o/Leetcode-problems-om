class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        A = []
        for x in asteroids:
            while A and x < 0 and A[-1] > 0:
                if A[-1] < abs(x):
                    A.pop()
                    continue
                elif A[-1] == abs(x):
                    A.pop()
                break  
            else:
                A.append(x)
        return A
                    