class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        A = []
        for x in s:
            if A is None:
                A.append(x)
            elif A and A[-1] == x :
                A.pop()
            else:
                A.append(x)
        return "".join(A)
