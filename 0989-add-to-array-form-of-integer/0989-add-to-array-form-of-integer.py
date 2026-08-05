class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        index = len(num) - 1
        ans = []
        while index >= 0 or k > 0:
            if index >= 0:
                k = k + num[index]
                index -= 1
            ans.append(k % 10)
            k //= 10
            
        return ans[::-1]