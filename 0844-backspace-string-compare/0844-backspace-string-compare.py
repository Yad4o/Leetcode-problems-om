class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def S(s):
            A = []
            for x in s:
                if x != '#':
                    A.append(x)
                else:
                    if A:
                        A.pop()
            return A
        return S(s) == S(t)