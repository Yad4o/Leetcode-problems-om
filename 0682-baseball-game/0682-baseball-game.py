class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        A = []
        result = 0
        for i in range(len(operations)):
            
            if operations[i] == '+':
                A.append(A[-1] + A[-2])
            elif operations[i] == 'C':
                A.pop()
            elif operations[i] == 'D':
                A.append(A[-1]*2)
            else:
                A.append(int(operations[i]))
        return sum(A)