class Solution(object):
    def pivotIndex(self, nums):
        T = sum(nums)
        L = 0
        for i in range(len(nums)):
            R = T - L - nums[i]
            if R == L:
                return i
            L += nums[i]
        return -1