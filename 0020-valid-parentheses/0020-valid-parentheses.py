class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        A = []
        for x in s:
            if x == '(' or x == '[' or x == '{':
                A.append(x)
            
            else: 
                if len(A) == 0:
                    return False
                elif x == ')' and A[-1] != '(':
                    return False
                elif x == ']' and A[-1] != '[':
                    return False
                elif x == '}' and A[-1] != '{':
                    return False
                else:
                    A.pop()
        return len(A) == 0