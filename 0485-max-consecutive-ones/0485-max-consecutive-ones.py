class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        maxcount = 0
        for x in nums:
            if x is 1:
                count += 1
                maxcount = max(maxcount, count)
            else:
                count = 0
        return maxcount