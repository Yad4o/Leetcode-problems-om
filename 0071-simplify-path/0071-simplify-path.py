class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        
        # Split by '/' automatically removes duplicate slashes (creates empty strings)
        components = path.split('/')
        
        for portion in components:
            if portion == '..' or portion == '':
                # If '..', go up one level by popping from stack (if stack isn't empty)
                if portion == '..' and stack:
                    stack.pop()
            elif portion != '.':
                # Any normal directory name (including '...', '....', 'a.') goes into the stack
                stack.append(portion)
                
        # Join components with '/' and ensure it starts with a leading '/'
        return "/" + "/".join(stack)