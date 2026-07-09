class Solution(object):
    def moveZeroes(self, nums):
        j = 0
        for i in range(0, len(nums)):
            if nums[j] == 0 and nums[i] != 0:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                j += 1
            elif nums[j] != 0:
                j += 1
        return nums