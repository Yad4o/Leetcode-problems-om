class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range (1, len(nums)):
            if nums[j] == 0 and nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
            elif nums[j] != 0 and nums[i] == 0 or nums[j] != 0 and nums[i] != 0:
                j += 1