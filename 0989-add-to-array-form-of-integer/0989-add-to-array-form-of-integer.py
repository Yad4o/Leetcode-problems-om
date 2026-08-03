class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        i = len(num) - 1
        ans = []
        while i >= 0 or k > 0:
            if i >= 0:
                k = k + num[i]
            ans.append(k % 10)
            k //= 10
            i -= 1
        return ans[::-1]