class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxword = 0
        current = 0
        for x in s:
            if x == ' ':
                if current != 0:
                    maxword += 1
                current = 0
            else:
                current += 1
        if current != 0:
            maxword += 1
        return maxword

        