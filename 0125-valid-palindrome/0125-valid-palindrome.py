class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        A = "".join(char.lower() for char in s if char.isalnum())
        j = len(A) -1
        i = 0
        while i < j:
            if not A:
                return True
            if A[i] != A[j]:
                return False
            i += 1
            j -= 1
        return True
            