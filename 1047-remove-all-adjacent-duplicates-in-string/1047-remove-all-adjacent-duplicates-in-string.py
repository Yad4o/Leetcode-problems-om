class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        A = []
        for x in s:
            if A and x == A[-1]:
                A.pop()
            else:
                A.append(x)
        return "".join(A) 