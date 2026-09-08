class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        A = []
        curr = ''
        for x in path + '/':
            if x == '/':
                if curr == '..':
                    if A:
                        A.pop()
                elif curr == '.' or curr == '':
                    pass
                else:
                    A.append(curr)
                
                curr = ''
            else:
                curr += x 
                
        return "/" + "/".join(A)
