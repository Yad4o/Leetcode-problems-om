class Solution(object):
    def reverseString(self, s):
        i = 0
        j = len(s) - 1
        for i in range(0, len(s)-1):
            if i <= j:
                s[i], s[j] = s[j], s[i]
                j -= 1