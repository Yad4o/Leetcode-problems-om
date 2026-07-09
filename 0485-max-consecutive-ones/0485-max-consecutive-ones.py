class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        maxcount = 0
        for x in nums:
            if x is 1:
                count += 1
                maxcount = max(maxcount, count)
            else:
                count = 0
        return maxcount