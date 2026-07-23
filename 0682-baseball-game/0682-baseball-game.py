class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        A = []
        for x in operations:
            if x == '+':
                A.append(A[-1] + A[-2])
            elif x == 'C':
                A.pop()
            elif x == 'D':
                A.append(A[-1] * 2)
            else :
                A.append(int(x))
        return sum(A)
        