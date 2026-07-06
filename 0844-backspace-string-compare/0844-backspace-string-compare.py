class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def S(a):
            A = []
            for x in a:
                if x == '#':
                    if A:
                        A.pop()
                else:
                    A.append(x)
            return "".join(A)
        return S(t) == S(s)