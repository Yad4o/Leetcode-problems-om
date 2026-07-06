class Solution(object):
    def isValid(self, s):
        A = []
        for i in range(len(s)):
            if s[i] == '(' or  s[i] == '[' or  s[i] == '{':
                A.append(s[i])
            else:
                if len(A) == 0:
                    return False
                top = A.pop()
                if not (s[i] == ')' and top == '(' or s[i] == ']' and top == '[' or s[i] == '}' and top == '{') :
                    return False
        return len(A)==0