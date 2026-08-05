class Solution:
    def findDisappearedNumbers(self, nums):

        for i in range(len(nums)):
            A = abs(nums[i]) - 1
            if nums[A] > 0:
                nums[A] *= -1
        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i + 1)
        return ans