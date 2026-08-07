class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxword = 0
        current = 0
        for x in s:
            if x == ' ':
                if current != 0:
                    maxword = current
                current = 0
            else :
                current += 1
        if current != 0:
            maxword = current
        return maxword