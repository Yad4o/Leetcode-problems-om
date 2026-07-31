class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        A = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[A] = nums[i]
                A += 1
        return A