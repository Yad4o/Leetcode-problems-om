class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            left = sum(nums[:i])
            right = sum(nums[i+1:])

            if left == right:
                return i
        return -1