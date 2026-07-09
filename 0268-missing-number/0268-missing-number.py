class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        A = n * (n + 1) // 2
        B = 0
        for x in nums:
            B += x
        return A - B